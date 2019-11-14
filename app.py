from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from dotenv import load_dotenv
from decouple import config
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


def get_doge():
    dogeData = requests.get('https://random.dog/woof.json').json()
    img_url = dogeData['url']
    return img_url


def get_joke():
    joke_data = requests.get('https://icanhazdadjoke.com', headers = {'Accept': 'application/json'}).json()
    joke = joke_data['joke']
    return joke


def joke(bot, update):
    joke = get_joke()
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = joke)

def boop(bot, update):
    doge_url = get_doge()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id = chat_id, photo = doge_url)


def main():
    updater = Updater(config('API_TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('boop',boop))
    dp.add_handler(CommandHandler('joke', joke))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
