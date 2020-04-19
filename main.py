import telebot
from telebot import types

bot = telebot.TeleBot('1203655746:AAH4uQhdBDYb3j3MiVzpWUuSLMaAFTzLNxI')

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть на сайте", url="https://translate.yandex.ru/"))
    bot.send_message(message.chat.id, "Вот ссылка", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['vk'])
def open_vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть ВК", url="https://vk.com/"))
    bot.send_message(message.chat.id, "Вот ссылка", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['inst'])
def open_inst(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть Inst", url="https://instagram.com/"))
    bot.send_message(message.chat.id, "Вот ссылка", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Словарь")
    btn2 = types.KeyboardButton("Переводчик")
    markup.add(btn1, btn2)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}! Что ты хочешь узнать?</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "словарь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Руcско-Чувашский")
        btn2 = types.KeyboardButton("Чувашско-Руcский")
        markup.add(btn1, btn2)
        final_message = "Выберете направление перевода"

    elif get_message_bot == "переводчик":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Руско-Чувашский")
        btn2 = types.KeyboardButton("Чувашско-Руский")
        markup.add(btn1, btn2)
        final_message = "Выберете направление перевода"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Словарь")
        btn2 = types.KeyboardButton("Переводчик")
        markup.add(btn1, btn2)
        final_message = "Словарь или Переводчик"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)