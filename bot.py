import os

import telebot

from utils import get_daily_horoscope


BOT_TOKEN = "5939324097:AAFV-OvkRog4T4fhL-tMiSMaWnw-8z4nvGA"

bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['vx', 'call'])
def send_welcome(message):
    bot.send_message(message.chat.id, "https://t.me/miaoTiYan/29")


@bot.message_handler(commands=['yuyue', 'yy'])
def send_website(message):
    bot.send_message(message.chat.id, "https://miaotiyan.cn/#/home")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "老板，臣妾还没学会这个命令")

# @bot.message_handler(commands=['horoscope'])
# def sign_handler(message):
#     text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
#     sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(sent_msg, day_handler)


# def day_handler(message):
#     sign = message.text
#     text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
#     sent_msg = bot.send_message(
#         message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(
#         sent_msg, fetch_horoscope, sign.capitalize())


# def fetch_horoscope(message, sign):
#     day = message.text
#     horoscope = get_daily_horoscope(sign, day)
#     data = horoscope["data"]
#     horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
#     bot.send_message(message.chat.id, "Here's your horoscope!")
#     bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "老板，臣妾还没学会这个命令")

if __name__=='__main__':
    bot.infinity_polling()

    while True:
        pass