from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6712478774:AAGLy-WkBix3w6NlIxcG2R51CQAoDMbslnw')
dp = Dispatcher(bot) 

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(
        types.KeyboardButton('Button 1', web_app=WebAppInfo(url='https://gemini.google.com')))
    await message.answer('Hello, my друг!', reply_markup=markup)

executor.start_polling(dp)

