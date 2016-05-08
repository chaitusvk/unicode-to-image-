#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#configuration
font_size=30
width=30
height=30
back_ground_color=(255,255,255)
font_color=(0,0,0)
unicode_text = u"\u0C05"

im  =  Image.new ( "RGB", (width,height), back_ground_color )
draw  =  ImageDraw.Draw ( im )
unicode_font = ImageFont.truetype("NTR.ttf", font_size)
draw.text ( (0,0), unicode_text, font=unicode_font, fill=font_color )
im.save("text2.jpg")
