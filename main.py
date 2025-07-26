from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.enums import ChatAction
import os
import requests
import random
import asyncio
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "")
BOT_NAME = os.environ.get("BOT_NAME", "")
START_IMG = os.environ.get("START_IMG", "https://files.catbox.moe/48hczp.jpg")
STKR = os.environ.get("STKR", "")
LLAMA_API = os.environ.get("LLAMA_API", "http://localhost:11434") # Ollama local default

# --- AI integration: call ollama/llama.cpp REST API ---
def generate_llama_reply(prompt):
    url = LLAMA_API.rstrip("/") + "/api/generate" # ollama endpoint
    payload = {
        "model": "llama2",  # or your Ollama model name. Ex: "llama3", "mistral", ...
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        return response.json().get("response", "Sorry, I could not generate a reply.")
    except Exception as e:
        print("AI error:", e)
        return "🤖 Sorry, my brain isn't working right now."

Mukesh = Client(
    "chat-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

MAIN = [
    [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
     InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}")],
    [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴍᴅs", callback_data="HELP")],
    [InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data='source'),
     InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHNL}")],
]

PNG_BTN = [
    [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}")],
]

HELP_BACK = [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="HELP_BACK")]]

START =f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
**➻ ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**
**──────────────────**
**➻ ᴜsᴀɢᴇ /chatbot [on/off]**
**๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help**
"""
SOURCE_TEXT = f"""**๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ**
"""
SOURCE_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton('sᴏᴜʀᴄᴇ', callback_data='hurr')],
    [InlineKeyboardButton(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
     InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="HELP_BACK")]
])
SOURCE = 'https://files.catbox.moe/2d32oj.mp4'
HELP_READ = """**ᴜsᴀɢᴇ ☟︎︎︎**
**➻ ᴜsᴇ** `/chatbot on` **ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**
**➻ ᴜsᴇ** `/chatbot off` **ᴛᴏ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**
**๏ ɴᴏᴛᴇ ➻ ʙᴏᴛʜ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛ-ʙᴏᴛ ᴏɴ/ᴏғғ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**

**➻ ᴜsᴇ** `/ping` **ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**
||©️ @ItsKapilYadav||"""

x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=random.choice(x)

# --- Group chatbot on/off memory (in RAM for easy Heroku deploy) ---
ACTIVE_CHATS = set()

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in Mukesh.get_chat_members(
            chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        )
    ]

# --- Must join channel (unchanged) ---
@Mukesh.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot, msg: Message):
    if not UPDATE_CHNL:
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
        except UserNotParticipant:
            if UPDATE_CHNL.isalpha():
                link = f"https://t.me/{UPDATE_CHNL}"
            else:
                chat_info = await bot.get_chat(UPDATE_CHNL)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo=START_IMG,
                    caption=(f"» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ]({link}) ʏᴇᴛ, "
                             f"ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !"),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=link)],
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the UPDATE CHANNEL  : {UPDATE_CHNL} !")

# --- Start & Help, unchanged except no sticker if STKR empty ---
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    accha = await m.reply_text(text=f"{g}")
    await asyncio.sleep(1)
    await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴜᴍ ꜱᴛᴀʀᴛɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.delete()
    if STKR:
        umm = await m.reply_sticker(sticker = STKR)
        await asyncio.sleep(1)
        await umm.delete()
    await m.reply_photo(
        photo = START_IMG,
        caption=START,
        reply_markup=InlineKeyboardMarkup(MAIN),
    )

@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(text = HELP_READ, reply_markup = InlineKeyboardMarkup(HELP_BACK))
    elif query.data == "HELP_BACK":
        await query.message.edit(text = START, reply_markup=InlineKeyboardMarkup(MAIN))
    elif query.data == 'source':
        await query.message.edit_text(SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
    elif query.data == 'hurr':
        await query.answer()
        await query.message.edit_text(SOURCE)

@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    await message.reply_photo(START_IMG, caption=HELP_READ, reply_markup=InlineKeyboardMarkup(HELP_BACK),)

@Mukesh.on_message(filters.command(['source', 'repo']))
async def source(bot, m):
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS, reply_to_message_id=m.id)

@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["","+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
    start = datetime.now()
    txxt = await message.reply("__ριиgιиg...__")
    await asyncio.sleep(0.25)
    await txxt.edit_text("__ριиgιиg.....__")
    await asyncio.sleep(0.35)
    await txxt.delete()
    end = datetime.now()
    ms = (end-start).microseconds / 1000
    await message.reply_photo(
        photo=START_IMG,
        caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [Kapil Yadav](https://t.me/{OWNER_USERNAME})||**",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

# ----- CHATBOT GROUP ENABLE/DISABLE LOGIC (now RAM-only) -----
@Mukesh.on_message(filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatbotofd(client, message):
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in await is_admins(chat_id):
            return await message.reply_text("You are not admin")
    if chat_id not in ACTIVE_CHATS:
        ACTIVE_CHATS.add(chat_id)
        await message.reply_text("Chatbot Disabled!")
    else:
        await message.reply_text("ChatBot Already Disabled")

@Mukesh.on_message(filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"], prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatboton(client, message):
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in await is_admins(chat_id):
            return await message.reply_text("You are not admin")
    if chat_id in ACTIVE_CHATS:
        ACTIVE_CHATS.remove(chat_id)
        await message.reply_text("ChatBot Enabled!")
    else:
        await message.reply_text("Chatbot Already Enabled")

@Mukesh.on_message(filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatbot(client, message):
    await message.reply_text("**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")

# ========== AI RESPONDER for PRIVATE & GROUPS (respects on/off in groups) ==========
@Mukesh.on_message(
    (filters.text | filters.sticker) &
    ~filters.bot
)
async def ai_handler(client, message: Message):
    if message.chat.type in ("group", "supergroup"):
        if message.chat.id in ACTIVE_CHATS:
            return # disabled
    # Give some prompt if sticker
    prompt = message.text
    if not prompt and message.sticker:
        prompt = f"A user sent a sticker {message.sticker.emoji or ''}. Respond in a fun chat way."
    if prompt:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        reply = generate_llama_reply(prompt)
        await message.reply_text(reply)

print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ! ʙᴏᴛ ʙʏ ɪᴛsᴋᴀᴘɪʟʏᴀᴅᴀᴠ")      
Mukesh.run()
