from Maxrobot.events import register
from Maxrobot import OWNER_ID
from Maxrobot import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Some Images by MaxRobot And Logo Maker Bot

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [ 
                         "./Katszuki/resources/download (1).png", 

                         "./Katszuki/resources/download (2).png",
                        
                         "./Katszuki/resources/download.png", 
                        
                         "./Katszuki/resources/images.png",
                         "./Katszuki/resources/photo_2021-10-12_23-41-57.jpg",
                          "./Katszuki/resources/1.jpg",
                          "./Katszuki/resources/2.jpg",
                          "./Katszuki/resources/3.jpg",
                          "./Katszuki/resources/loli 1.jpg",
                          "./Katszuki/resources/loli 2.jpg",
                          "./Katszuki/resources/loli 3.jpg",
                          "./Katszuki/resources/loli 4.jpg",
                          "./Katszuki/resources/loli 5.jpg",
                          "./Katszuki/resources/loli 6.jpg",
                          "./Katszuki/resources/loli 7.jpg",
                          "./Katszuki/resources/loli 8.jpg",
                          "./Katszuki/resources/loli 9.jpg",
                          "./Katszuki/resources/loli 10.jpg"
                         
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('♻ Wait..now ok!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(TELEGRAPH_MEDIA_LINKS))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Katszuki/resources/neon.ttf",40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="yellow")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Katszuki_Bot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @EmoBotDevolopers  to use this, {e}')
    
    
@register(pattern="^/lolilogo ?(.*)")
async def logo(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('♻ Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Katszuki/resources/loli 1.png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Katszuki/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Max123robot🇱🇰")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @EmoBotDevolopers  to use this, {e}')

  

@register(pattern="^/pandalogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('♻ Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Katszuki/resources/pandabg.png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Katszuki/resources/font.otf", 100)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Katszuki_Bot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @EmoBotDevolopers  to use this, {e}')


# Katszuki Loli Logos Is Added by ImRishmika

@register(pattern="^/Katszukilogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('♻ Wait..now ok!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(TELEGRAPH_MEDIA_LINKS))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Katszuki/resources/neon.ttf",40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="yellow")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Katszuki_Bot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @EmoBotDevolopers  to use this, {e}')
    


  
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
@Max123robot🇱🇰
 ❍ /logo text :  Create your logo with your name
 ❍ /Katszukilogo text :  Create your logo with your name
 ❍ /lolilogo text :  Create your logo with your name
 ❍ /pandalogo :  Create your logo with your name
 """
__mod_name__ = "Logo Maker"
