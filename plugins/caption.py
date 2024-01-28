from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *




@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("<b>Give me a caption to set.\n\nExample:- `/set_caption File Name`</b>")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("<b>Your Caption successfully added ✅</b>")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("<b>You dont have any custom caption</b>")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("<b>Your caption successfully deleted ✅</b>")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("<b>You dont have any custom caption</b>")
          
