import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token = "8210782460:AAHK6dInuvZduJ_vtfYZT01qgNkN6CrPNEE",
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message(F.command("start"))
async def start(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"Привет, {user_name}! 👋\n\nЯ Эхобот на aiogram 3.\nОтправь мне любое сообщение, и я повторю его."
    )

@dp.message(F.command("help"))
async def help(message: Message):
    await message.answer("Команды:\n/start — начать\n/help — помощь\n/info — информация")

@dp.message(F.command("info"))
async def info(message: Message):
    await message.answer("Пробный телеграм-бот. Дата создания: 04.12.2024")

@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


