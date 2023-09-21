from aiogram.utils import executor
from aiogram import types
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
import os

load_dotenv()

scheduler = AsyncIOScheduler(timezone="Europe/Minsk")

bot = Bot(token=os.environ.get('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)
ID = 1160001485
id = 644784412
emoji_love = ['🤍', '💋', '❤️‍🩹', '❤️‍🔥', '💌', '🫂', '✨']
emoji_sad = ['😬', '🤥', '😔', '😴', '😪', '😕', '😟', '🙁', '☹', '😮', '😯', '😲', '😳',
             '😦', '😧', '😖', '😣', '😭', '😢', '😥', '😰', '😞', '😓', '😿']

b2 = KeyboardButton('123 признания родной душе')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b2)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.from_user.id == id:
        await message.answer("Привет", reply_markup=kb_client)
    elif message.from_user.id == ID:
        await message.answer("Привет", reply_markup=kb_client)
    else:
        emoji_select_sad = random.choice(emoji_sad)
        await message.answer("У вас нет доступа к этой команде " + emoji_select_sad)



@dp.message_handler(lambda message: '123 признания родной душе' in message.text)
async def compliment_command(message: types.Message):
    if message.from_user.id == id:
        with open('compliments.json', 'r', encoding='utf-8') as f:
            read = f.read()
        compliments = read.split('\n')
        compliment = random.choice(compliments)
        emoji_select_love = random.choice(emoji_love)
        await message.answer(f"<span class='tg-spoiler'>{compliment + ' ' + emoji_select_love}</span>", parse_mode="HTML")
    elif message.from_user.id == ID:
        with open('compliments.json', 'r', encoding='utf-8') as f:
            read = f.read()
        compliments = read.split('\n')
        compliment = random.choice(compliments)
        emoji_select_love = random.choice(emoji_love)
        await message.answer(f"<span class='tg-spoiler'>{compliment + ' ' + emoji_select_love}</span>", parse_mode="HTML")
    else:
        emoji_select_sad = random.choice(emoji_sad)
        await message.answer("У вас нет доступа к этой команде " + emoji_select_sad)


@dp.message_handler()
async def meeting_command(message: types.Message):
    emoji_select_sad = random.choice(emoji_sad)
    i_dont_understand_you = 'Я тебя не понимаю '
    await message.answer(i_dont_understand_you + emoji_select_sad + '\n\n\nНажми /start')

async def autocompliments_for_ID():
    with open('compliments.json', 'r', encoding='utf-8') as f:
        read = f.read()
    compliments = read.split('\n')
    compliment = random.choice(compliments)
    emoji_select_love = random.choice(emoji_love)
    await bot.send_message(ID, f"<span class='tg-spoiler'>{compliment + ' ' + emoji_select_love}</span>", parse_mode="HTML")


async def autocompliments_for_id():
    with open('compliments.json', 'r', encoding='utf-8') as f:
        read = f.read()
    compliments = read.split('\n')
    compliment = random.choice(compliments)
    emoji_select_love = random.choice(emoji_love)
    await bot.send_message(id, f"<span class='tg-spoiler'>{compliment + ' ' + emoji_select_love}</span>", parse_mode="HTML")



def schedule_jobs():
    scheduler.add_job(autocompliments_for_ID,  'cron', day_of_week='mon-sun', hour=20, minute=36)
    scheduler.add_job(autocompliments_for_id,  'cron', day_of_week='mon-sun', hour=20, minute=36)


async def on_startup(dp):
    schedule_jobs()

if __name__ == '__main__':
    while True:
        try:
            scheduler.start()
            executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
        except:
            time.sleep(5)