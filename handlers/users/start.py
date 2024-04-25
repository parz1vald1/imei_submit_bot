from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.Userstates import IMEISendAllowance
from data.config import HR, ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await db.select_vba(telegram_id=message.from_user.id)
    ad_hr_id = str(message.from_user.id)
    if ad_hr_id in ADMINS:
        await message.answer("You have the ultimate permission.")
    elif ad_hr_id in HR:
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam",
                "/add_VBA - VBA qo'shish"
                )
        await message.answer("\n".join(text))
    elif user and user[7] == message.from_user.id:
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam",
                "/add_IMEI - IMEI qo'shish"
                )
        await message.answer("\n".join(text))
        await IMEISendAllowance.permission_granted.set()
    else:
        await message.answer("You have no permission")
