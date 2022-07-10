import telebot
from telebot import types  # для меню
import random

TOKEN = "5468638476:AAHT0uziVEkhTH5BMolGwZbbXCdkDWxkHRU"

bot = telebot.TeleBot(TOKEN)  # For token
hello = 'Hello'


@bot.message_handler(commands=['start'])  # для отслеживания команд
def start(message):
    bot.send_message(message.chat.id, 'Hello')  # в чат айди запрашиваем айди чата для обратной отправки сообщений
    # print(message.from_user)
    bot.send_message(message.chat.id,
                     'Приветствую тебя страник телеграм ботов ' +
                     "<i>" + message.from_user.first_name + "</i>" +
                     ' Также известный как ' +
                     "<b>" + message.from_user.username + "</b>",

                     parse_mode='html')
    startMenu(message)
def startMenu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Рандомное число 1-20')
    btn2 = types.KeyboardButton("Рандомное число 0-1")
    btn3 = types.KeyboardButton("Старт")
    btn4 = types.KeyboardButton("Сайт")

    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Вот тебе менюшка', reply_markup=markup)


@bot.message_handler(commands=['website'])
def photo(message):
    btn = types.InlineKeyboardMarkup()  # Создание элемента
    btn.add(types.InlineKeyboardButton("Ссылка на сайт", url='https://google.com'))  # Создание кнопки которая встраивается в сообщение
    bot.send_message(message.chat.id, 'Вот туда ->', reply_markup=btn)  # Отправка ответа пользователю


@bot.message_handler(commands=['menu'])
def menu(message):
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2)  # resize_keyboard=True кнопки подстраиваются под размер экрана row_width= - количество кнопок в ряду
    starts = types.KeyboardButton('Меню')
    site = types.KeyboardButton('Site')
    btn.add(starts, site)
    bot.send_message(message.chat.id, 'Used menu', reply_markup=btn)


@bot.message_handler(content_types=['text'])  # Проверка сообщений на данный текст
def getUserInfo(message):
    if message.text == 'Что ты знаешь обо мне?':
        bot.send_message(message.chat.id, message)
    if message.text == 'Что такое':
        btn = types.InlineKeyboardMarkup()  # Создание элемента
        btn.add(types.InlineKeyboardButton("Это", url='https://google.com'))  # Создание кнопки
        bot.send_message(message.chat.id, 'Вот туда ->')

    if message.text == "Рандомное число 1-20":
        bot.send_message(message.chat.id, 'Вам выпало: ' + str(random.randint(1, 20)))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Новое число 1-20')
        btn2 = types.KeyboardButton("В меню")

        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Число от 1 до 20', reply_markup=markup)

    if message.text == "Рандомное число 0-1":
        bot.send_message(message.chat.id, "Рандомное число 0-1, выпало: " + str(random.randint(0, 1)))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn4 = types.KeyboardButton('Новое число 0-1')
        btn5 = types.KeyboardButton("В меню")

        markup.add(btn4, btn5)
        bot.send_message(message.chat.id, 'Число от 0 до 1', reply_markup=markup)

    if message.text == "Сайт":
        btn6 = types.InlineKeyboardMarkup()
        btn6.add(types.InlineKeyboardButton("Это", url='https://google.com'))
        bot.send_message(message.chat.id, 'Вот мой любимый', reply_markup=btn6)
    if message.text == "Старт":
        startMenu(message)
        # bot.send_message(message.chat.id, '', '/start')
    if message.text == "В меню":
        startMenu(message)
        # bot.send_message(message.chat.id, '', '/start')
    if message.text == 'Новое число 0-1':
        bot.send_message(message.chat.id, "Новое число 0-1: " + str(random.randint(0, 1)))
    if message.text == 'Новое число 1-20':
        bot.send_message(message.chat.id, 'Новое число 1-20: ' + str(random.randint(1, 20)))


bot.polling(none_stop=True)  # Бесконечный цикл

# @bot.message_handler(content_types=['sticker'])  #content_types=['photo', 'audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'] @можно указывать несколько
# def sendAqnswerStiker(message):
