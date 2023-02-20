#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("25906376", default=None, cast=int)
API_HASH = config("27573285f886c6b3a647f5656d56bbb1", default=None)
BOT_TOKEN = config("6132685416:AAFLbmlOO1x_ZWwSSok4U_5XzmTprhapu8U", default=None)
SESSION = config("AgA55ZOninwap271VdKbdpzLass8PFwa0ta5Pb75PI8zgc0ghC-ZhjGwmK4eTwmE1rxcputyphjuRIGC0qd55lvPZ0fZ9hzVP9SqD08_SUEXOQ8U_MM95AGUXBrRksBFdzt1fj8WF6mdCJogpKBjLfaNLjvQeWmHI73TqSwdaanw-QbB_6kL17HWlS0qhPWWPtLViU4aVLyUO8zrCmFXhwWkmY1fkTrhnpIV4l5n3I9BaDFleEIsA6HN7TaZ2eMdXMU5Prt2kuJNFivXl_e261xrSoX0dPCvuLpbdvrBQQWOs-fn3MLn0wJjwoM3Vdi__DQnIIvkRohWPFvVDVnl3LP0AAAAATT_0QMA", default=None)
FORCESUB = config("hackers_assemble", default=None)
AUTH = config("737870357", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
