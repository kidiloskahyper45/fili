#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(861055237)
    return expires_at

@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):

      if 'help' in update.data:
          await update.message.delete()
          await help_user(bot, update.message)

      if 'close' in update.data:
          await update.message.delete()
 
      if 'about' in update.data:
          await update.message.edit(text=Translation.ABOUT_1, 
                #parse_mode='markdown' 
                disable_web_page_preview=True,
                #reply_to_message='update.message_id',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [        
                            InlineKeyboardButton('🔐 Close', callback_data='close'),
                            InlineKeyboardButton('🔙 Back', callback_data='help')
                        ]
                    ] 
                )
           )
          


         
                   
@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('✅  Other Bots ', url='https://t.me/TG_BotZ/33'),
                    InlineKeyboardButton('Share & Support Me', url='https://t.me/share/url?url=Hai%20Friend%2C%0D%0AAm%20Introducing%20a%20Powerful%20%2A%2ARename%20Bot%2A%2A%20for%20Free.%0D%0A%2A%2ABot%20Link%2A%2A%20%3A%20%40TGRename_Bot')
                ],
                [
                    InlineKeyboardButton('⚒️ About Me', callback_data='about'),
                    InlineKeyboardButton('🔐 Close', callback_data='close')
                ]
            ] 
        )
        #reply_to_message_id=update.message_id
    ) 

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about_meh(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_USER,
        #parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [        
                    InlineKeyboardButton('🔐 Close', callback_data='close')
                ]
            ] 
        ),
        reply_to_message_id=update.message_id
    )

@Client.on_message(Filters.private & Filters.command("start") & Filters.text)
async def start(bot,update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start") 
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
          
                [
                    InlineKeyboardButton('⚙️ Help', callback_data='help'),
                    InlineKeyboardButton('🔐 Close', callback_data='close')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["plan"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/plan")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.PLAN_TEXT.format(update.from_user.first_name),
        #parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    ) 
