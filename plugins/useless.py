from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Bot.on_message(filters.command('followus') & filters.private)
async def followus(bot: Bot, message: Message):
    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton('𝓜𝓸𝓿𝓲𝓮𝓼 𝓖𝓻𝓸𝓾𝓹', url="t.me/+ADvUFRV3nsljNTM1"),
                          InlineKeyboardButton('𝓤𝓹𝓭𝓪𝓽𝓮𝓼 𝓒𝓱𝓪𝓷𝓷𝓮𝓵', url="t.me/MoviezAddaKan")
                       ],[
                          InlineKeyboardButton("𝓑𝓸𝓽 𝓞𝔀𝓷𝓮𝓻", url="t.me/captblacknight")
                         ]
                        ]
                    )
    await message.reply(f"<b>𝓕𝓸𝓵𝓵𝓸𝔀 𝓤𝓼 </b>\n\n", reply_markup=reply_markup, disable_web_page_preview = True)


@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
        
        
