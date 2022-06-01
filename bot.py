import telebot
import os
os.system('cls')

TOKEN = "5485770455:AAGdERF3tdhEsZMkRjoF3H0iqaw9CBjZcCI"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(
        message.chat.id, 'Привет, когда я вырасту, я буду БОЛЬШИМ!')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет" or text == "Привет!" or text == "Привет" or text == "привет!":
        bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
    elif text == "как дела?" or text == "как дела":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я Вас не понял :(')


@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво!')


bot.polling()
