#(©)CodeXBotz




import os
import asyncio
from asyncio import sleep
from contextlib import suppress
from pyrogram import Client, filters, __version__
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant, RPCError

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user


async def forcedjoined(c: Client, m: Message, tryag: str = ""):
    if m.chat.type != ChatType.PRIVATE:
        return 1
    with suppress(UserIsBlocked):
        try:
            try:
                u = await c.get_chat_member(-1001680440476, m.from_user.id)
            except FloodWait as fo:
                await sleep(fo.value + 1)
                u = await c.get_chat_member(-1001680440476, m.from_user.id)
            if u.status in (ChatMemberStatus.BANNED,
                            ChatMemberStatus.RESTRICTED):
                await m.reply_text(
                    text="Sorry, You are Banned!\nNow You Can't Use Me.",
                    disable_web_page_preview=True,
                )
                return 0
            try:
                u = await c.get_chat_member(-1001673528398, m.from_user.id)
            except FloodWait as fo:
                await sleep(fo.value + 1)
                u = await c.get_chat_member(-1001673528398, m.from_user.id)
            if u.status in (ChatMemberStatus.BANNED,
                            ChatMemberStatus.RESTRICTED):
                await m.reply_text(
                    text="Sorry, You are Banned!\nNow You Can't Use Me.",
                    disable_web_page_preview=True,
                )
                return 0
            try:
                u = await c.get_chat_member(-1001829070430, m.from_user.id)
            except FloodWait as fo:
                await sleep(fo.value + 1)
                u = await c.get_chat_member(-1001829070430, m.from_user.id)
            if u.status in (ChatMemberStatus.BANNED,
                            ChatMemberStatus.RESTRICTED):
                await m.reply_text(
                    text="Sorry, You are Banned!\nNow You Can't Use Me.",
                    disable_web_page_preview=True,
                )
                return 0
            try:
                u = await c.get_chat_member(-1001487979336, m.from_user.id)
            except FloodWait as fo:
                await sleep(fo.value + 1)
                u = await c.get_chat_member(-1001487979336, m.from_user.id)
            if u.status in (ChatMemberStatus.BANNED,
                            ChatMemberStatus.RESTRICTED):
                await m.reply_text(
                    text="Sorry, You are Banned!\nNow You Can't Use Me.",
                    disable_web_page_preview=True,
                )
                return 0
            try:
                u = await c.get_chat_member(-1001668949698, m.from_user.id)
            except FloodWait as fo:
                await sleep(fo.value + 1)
                u = await c.get_chat_member(-1001668949698, m.from_user.id)
            if u.status in (ChatMemberStatus.BANNED,
                            ChatMemberStatus.RESTRICTED):
                await m.reply_text(
                    text="Sorry, You are Banned!\nNow You Can't Use Me.",
                    disable_web_page_preview=True,
                )
                return 0
        except UserNotParticipant:
            if tryag:
                mark = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 1! ✅ ", url="https://t.me/Movies7xBoTs")
                    ],
                [
                    InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 2! ✅", url="https://t.me/Anime7x")
                ],
                [
                    InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 3! ✅", url="https://t.me/OnLyFans_OnlYFap")
                ],
                [
                    InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 4! ✅", url="https://t.me/Movies7x")
                ],
                [
                    InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 5! ✅", url="https://t.me/DraMaLiNKz")
                ],
                    [
                        InlineKeyboardButton("🔖 𝘾𝙝𝙚𝙘𝙠 𝙨𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙨𝙩𝙖𝙩𝙪𝙨💠", url=tryag)
                    ]
                ])
            else:
                mark = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 1! ✅", url="https://t.me/Movies7xBoTs")
                    ],
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 2! ✅", url="https://t.me/Anime7x")
                    ],
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 3! ✅", url="https://t.me/OnLyFans_OnlYFap")
                    ],
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 4! ✅", url="https://t.me/Movies7x")
                    ],
                    [
                        InlineKeyboardButton("🚀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗹𝗶𝗻𝗸 5! ✅", url="https://t.me/DraMaLiNKz")
                    ],
                ])
            await m.reply_text(
                text="<b> 🍁 𝖳𝗈 𝖺𝖼𝖼𝖾𝗌𝗌 𝗈𝗎𝗋 𝖻𝗈𝗍'𝗌 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌, 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾 𝗍𝗈 𝗍𝗁𝖾𝗌𝖾 5 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝗅𝗂𝗇𝗄 𝗉𝗋𝗈𝗏𝗂𝖽𝖾𝖽 𝖻𝖾𝗅𝗈𝗐. 🌟 𝖶𝗂𝗍𝗁 𝗈𝗎𝗋 𝖻𝗈𝗍, 𝗌𝖾𝖺𝗋𝖼𝗁 𝗆𝗈𝗏𝗂𝖾𝗌/𝗌𝖾𝗋𝗂𝖾𝗌 𝖻𝗒 𝗇𝖺𝗆𝖾 𝖺𝗇𝖽 𝖺𝖼𝖼𝖾𝗌𝗌 𝖺𝖽-𝖿𝗋𝖾𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇𝗌𝗍𝖺𝗇𝗍𝗅𝗒 📥 </b>",
                reply_markup=mark,
            )
            return 0
        except RPCError:
            await m.reply_text(
                text="Something went Wrong.",
                disable_web_page_preview=True,
            )
            return 0
        return 1
    return 0


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    if not await forcedjoined(client, message, f"https://t.me/{client.me.username}?start={message.text.split(maxsplit=1)[1:][0]}" if len(message.text.split(maxsplit=1)) > 1 else ""):
        return
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

    
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

    
    
@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
