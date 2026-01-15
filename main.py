import logging
from aiogram import Bot, Dispatcher, executor, types
import yt_dlp
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("🎥 YouTube / TikTok / Instagram link yuboring")

@dp.message_handler()
async def download(msg: types.Message):
    url = msg.text
    await msg.answer("⏳ Yuklanmoqda...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s',
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir():
            if file.startswith("video."):
                await msg.answer_video(open(file, "rb"))
                os.remove(file)
                break
    except:
        await msg.answer("❌ Xatolik. Linkni tekshir.")

if __name__ == '__main__':
    executor.start_polling(dp)
