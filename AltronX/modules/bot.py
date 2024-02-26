import os
import sys
import heroku3
from datetime import datetime
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"•[ 🤍🖤️ #ᴛᴇᴀᴍ_4ѕт_ғɪɢʜᴛᴇʀ 🖤🤍️ ]•", parse_mode=None, link_preview=None)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await e.reply(f"➲ #4sᴛ_ʀᴇᴀᴅʏ_ғᴏʀ_ғᴜᴄᴋɪɴɢ 💦💘\n\n➲ sᴜᴅᴏ ▸ @ll4st_MIND_GAMERII\n\n➲ 🍷 ᴘɪɴɢ ▸ `{mp} ms`")


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"➲ ʀᴇʙᴏᴏᴛ ᴅᴏɴᴇ ~ ʙsᴅᴋᴇ 😤\n➲ 2 ᴍɪɴᴛ ᴡᴀɪᴛ ᴘʟᴇᴀsᴇ\n➲ #ᴍᴏʀᴇ_ᴘᴏᴡᴇʀғᴜʟʟ_4sᴛ 💘")
        try:
            await MK1.disconnect()
        except Exception:
            pass
        try:
            await MK2.disconnect()
        except Exception:
            pass
        try:
            await MK3.disconnect()
        except Exception:
            pass
        try:
            await MK4.disconnect()
        except Exception:
            pass
        try:
            await MK5.disconnect()
        except Exception:
            pass
        try:
            await MK6.disconnect()
        except Exception:
            pass
        try:
            await MK7.disconnect()
        except Exception:
            pass
        try:
            await MK8.disconnect()
        except Exception:
            pass
        try:
            await MK9.disconnect()
        except Exception:
            pass
        try:
            await MK10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USER", None)

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"🍃 #_4sᴛ_ɢᴀᴛᴛɪɴɢ_ᴍᴏʀᴇ_sᴛʀᴏɴɢ 🍃")
        mks = "SUDO_USER"
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except Exception:
            await ok.edit("ᴀʙᴇ ᴊʜᴀᴛ ʙᴀᴀʟ ᴍᴇᴋᴏ ʀᴇᴘʟʏ ᴅᴇ ʀᴀʜᴀ ʜᴀɪ ʀᴜᴋ ᴛᴇʀɪ ᴍᴀ ᴄʜᴏᴅᴛᴀ ᴀʙʜɪ")
        if len(sudousers) > 0:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f":❤️⧽ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ 4sᴛ ᴛᴇᴀᴍ \n:🤍⧽ ɴᴇᴡ ᴜsᴇʀ ɪᴅ : `{target}`\n:🖤⧽ 𝖩𝖮𝖨𝖭 :- @I_M_FIGHTER")
        heroku_var[mks] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(GetFullUserRequest(previous_message.forward.sender_id))
        else:
            replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    return replied_user.user.id
