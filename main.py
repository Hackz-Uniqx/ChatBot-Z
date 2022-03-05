import os
import telebot

bot = telebot.TeleBot("5113140197:AAGFbo4U1VKtCuIuGYzVRneQ4YUfZp4b4GI")

@bot.message handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hi, I'm ChatBot-Z")

@bot.message handler(commands=["how"])
def send_message(message):
    bot.seng_message(message,"Nothing is here to worry about !!!")

bot.polling()