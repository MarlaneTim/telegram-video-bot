import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# 🔹 Укажи свой токен бота
TOKEN = "7777039374:AAGQ-vECP_YfDG2yBbWurfQdLBFb5vqmC0A"

# 🔹 Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔹 Обработчик команды /start
@dp.message()
async def start(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот 😊")

# 🔹 Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

# 🔹 Запускаем бота
if __name__ == "__main__":
    asyncio.run(main())
