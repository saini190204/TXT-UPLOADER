# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
import mmap
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/EX_MAFIYA",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/EX_MAFIYA",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/EX_MAFIYA",
            ),
            
        ],
    ]
)



Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/EX_MAFIYA",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/EX_MAFIYA",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Join to Check My Status ",
                url="https://t.me/EX_MAFIYA",
            ),
            
        ],
    ]
)


@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Choose a random image URL from the list
    random_image_url = ("https://graph.org/file/95a9fc09cc310c0c8cd6f.jpg")
    
    
    # Caption for the image
    caption = f"**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 ᡕᠵ᠊ᡃ່࡚ࠢ࠘ ⸝່ࠡࠣ᠊߯᠆ࠣ࠘ᡁࠣ࠘᠊᠊ࠢ࠘𐡏 —͟͞͞ MΛFIΛ☣ 👋!\n\n➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n➠ Can Extract Videos & Pdf Form Your Text File and Upload to Telegram\n\n➠ 𝐔𝐬𝐞 /drm 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞  \n\n➠𝐌𝐚𝐝𝐞 𝐁𝐲: @EX_MAFIYA **\n"
    
    # Send the image with the caption
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**🚯 ꜱᴛᴏᴘᴘᴇᴅ 🚯**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["drm"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝕤ᴇɴᴅ ᴛxᴛ ғɪʟᴇ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality")
    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[『 𝐁𝐢𝐬𝐡𝐧𝐨𝐢 ™』❤️]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"
    
    

    await editable.edit("**🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏\nᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄᴏᴀᴄʜɪɴɢ ᴀᴘᴘ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3
   
    await editable.edit("🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏")    
    input6 = message = await bot.listen(editable.chat.id)    
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif "tencdn.classplusapp" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "media-cdn.classplusapp" in url:
            	url = f"https://drm-api-six.vercel.app/api/cp/dl?url={url}"
            	
            elif "cwmediabkt99.crwilladmin.com" in url:
            	url = url.replace(' ', '%20')
            elif ".pdf*abcdefg" in url:
             a = url.replace('*abcdefg', '')
             url = a
            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[ 🎥 ] 𝗟ᴇᴄ ɪᴅ. » {str(count).zfill(3)}\n**<pre>🌟 𝗔ᴘᴘ 𝗡ᴀᴍᴇ** » {MR}<pre>**\n**\n**🔰 𝗧ɪᴛᴛʟᴇ** » {name1}**({res})**.mp4\n**<pre><code>📲 𝗕ᴀᴛᴄʜ 𝗡ᴀᴍᴇ** »**\n\n**{raw_text0} </code></pre>**\n\n**📛 𝗗ᴏᴡɴʟᴏᴀᴅᴇᴅ 𝗕ʏ » 🇮🇳 𝗝ᴀɪ 𝗦ʜʀᴇᴇ 𝗥ᴀᴍ 🇮🇳**\n\n'    
                ccyt = f'**[ 🎥 ] 𝗟ᴇᴄ ɪᴅ. » {str(count).zfill(3)}\n**<pre>🌟 𝗔ᴘᴘ 𝗡ᴀᴍᴇ** » {MR}<pre>**\n**\n**🔰 𝗧ɪᴛᴛʟᴇ** » {name1}**({res})**.mp4\n\n**🕹️ 𝗬ᴏᴜ𝗧ᴜʙᴇ 𝗟ɪɴᴋ »**\n**{url}\n**<code><pre>📲 𝗕ᴀᴛᴄʜ 𝗡ᴀᴍᴇ** »**\n\n**{raw_text0} </code></pre>**\n\n**📛 𝗗ᴏᴡɴʟᴏᴀᴅᴇᴅ 𝗕ʏ » 🇮🇳 𝗝ᴀɪ 𝗦ʜʀᴇᴇ 𝗥ᴀᴍ 🇮🇳**\n\n'
                cc1 = f'**[ 📁 ] 𝗣ᴅғ ɪᴅ. » {str(count).zfill(3)}\n**<pre>🌟 𝗔ᴘᴘ 𝗡ᴀᴍᴇ** » {MR}<pre>**\n**\n**🔰 𝗧ɪᴛᴛʟᴇ** » {name1} **({res})**.pdf \n**<pre><code>📲 𝗕ᴀᴛᴄʜ 𝗡ᴀᴍᴇ** »**\n\n**{raw_text0} </code></pre>**\n\n**📛 𝗗ᴏᴡɴʟᴏᴀᴅᴇᴅ 𝗕ʏ » 🇮🇳 𝗝ᴀɪ 𝗦ʜʀᴇᴇ 𝗥ᴀᴍ 🇮🇳**\n'                
                if "*" in url:
                     a, k = url.split("*", 1)
                     url = a
                     key = k
                     try:
                      	if ".pdf" in a:
                      		Show = f"**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥**\n\n**📚❰Name❱** `{name}\n🔗𝗧ᴏᴛᴀʟ 𝗟ɪɴᴋ𝘀 » {len(links)}\n📊𝗖ᴜʀʀᴇɴᴛʟʏ 𝗢ɴ » {str(count).zfill(3)}\n🐲𝗤ᴜᴀʟɪᴛʏ » {raw_text2}`\n🌿**Url**» {url}\n\nᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [『 𝐁𝐢𝐬𝐡𝐧𝐨𝐢 ™』❤️]**\n**🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏 **"
                      		prog = await m.reply_text(Show)
                      		file_path = await helper.download_file(url, name)
                      		copy = helper.decrypt_file(file_path, key)
                      		filename = file_path
                      		await prog.delete(True)
                      		await bot.send_document(chat_id=m.chat.id, document=filename, caption=cc1)
                      		count += 1
                      	else:
                      		Show = f"**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥**\n\n**📚❰Name❱** `{name}\n🔗𝗧ᴏᴛᴀʟ 𝗟ɪɴᴋ𝘀 » {len(links)}\n📊𝗖ᴜʀʀᴇɴᴛʟʏ 𝗢ɴ » {str(count).zfill(3)}\n🐲𝗤ᴜᴀʟɪᴛʏ » {raw_text2}`\n🌿**Url**» {url}\n\nᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [『 𝐁𝐢𝐬𝐡𝐧𝐨𝐢 ™』❤️]**\n**🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏 **"
                      		prog = await m.reply_text(Show)
                      		file_path = await helper.download_file(url, name)
                      		copy = helper.decrypt_file(file_path, key)
                      		filename = file_path
                      		await prog.delete(True)
                      		await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                      		count += 1
                     except FloodWait as e:
                      await m.reply_text(str(e))
                      time.sleep(1)
                      continue
                
                elif "drive" in url or ".ws" in url or "cwmediabkt99.crwilladmin.com" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(2)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥**\n\n**📚❰Name❱** `{name}\n🔗𝗧ᴏᴛᴀʟ 𝗟ɪɴᴋ𝘀 » {len(links)}\n📊𝗖ᴜʀʀᴇɴᴛʟʏ 𝗢ɴ » {str(count).zfill(3)}\n🐲𝗤ᴜᴀʟɪᴛʏ » {raw_text2}`\n🌿**Url**» {url}\n\nᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [『 𝐁𝐢𝐬𝐡𝐧𝐨𝐢 ™』❤️]**\n**🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏 **"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥 failed [『 𝐁𝐢𝐬𝐡𝐧𝐨𝐢 ™』❤️]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n🙏𝗝⃠ᴀɪ 𝗦⃠ʜʀᴇᴇ 𝗥⃠ᴀᴍ🙏"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("** ʟɪsᴛ ɪɴᴅᴇx ᴏᴜᴛ ᴏғ ʀᴀɴɢᴇ **")
    await m.reply_text("** 🔰 Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Aʟʟ Lᴇᴄᴛᴜʀᴇs...! 🔰 **")


bot.run()
