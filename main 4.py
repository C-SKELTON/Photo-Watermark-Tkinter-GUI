from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")
#input original image here
original_image = os.getenv("org_picture")

window = Tk()
window.title("Add Watermark")
window.config(padx=100, pady=200)
window.minsize(width=600, height=400)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Add Watermark")
my_label.grid(column=0, row=0, columnspan=4)
my_label.config(padx=15, pady=25)

#Input
canvas = Canvas(width=1000, height=224, bg='#FFFFFF', highlightthickness=0)
input = Entry(window,width = 30)
input.grid(column=1, row=5, columnspan=3)

#text
text = Text(window, width=48, height=1)
text.insert('1.0', 'Enter watermark text or file path to the right:')
text.grid(column=0,row=5)

text2 = Text(window, width=52, height=1)
text2.insert('1.0', 'For filepath replace backslash(\) with frontslash(/)')
text2.grid(column=0,row=6, columnspan=2)

var = StringVar()
l = Label(window, bg='white', width=20, text='Select a below option')
l.grid(row=2, columnspan=1)


def print_selection():
  choice = var.get()
  if choice == 'text':
      output = 'a'
  else:
      output = 'b'

  return(output)


def open_user_image():
    user_image = Image.open(original_image)
    ImageDraw.Draw(user_image)
    user_image.show()

def watermark_text_button_clicked():
    watermark_text = input.get()
    return watermark_text


def edit_user_image():
    text = watermark_text_button_clicked()
    if print_selection() == 'a':
        myfont = ImageFont.truetype('arial.ttf', 18)
        img = Image.open(original_image)
        img_update = ImageDraw.Draw(img)
        img_update.text((28,39), text, fill=(255,0,0), font=myfont)
        img.save(os.getenv("updated_text_watermark_image")) #update this to your save filepath location
        img.show()
    else:
        size = (200, 50)
        watermark_image = Image.open(text)
        base_image = Image.open(original_image)
        crop_image = watermark_image.copy()
        crop_image.thumbnail(size)
        copied_image = base_image.copy()
        copied_image.paste(crop_image, (500, 200))
        copied_image.show()
        copied_image.save(os.getenv("updated_photo_watermark_image"))

Radiobutton(window, text='Text watermark', variable=var, value='text', command=print_selection).grid(row=3, columnspan=1)
Radiobutton(window, text='Image watermark', variable=var, value='image', command=print_selection).grid(row=4, columnspan=1)

original_picture = Button(text='Show original picture', highlightthickness=0, command=open_user_image)
original_picture.grid(column=2,row=2)

user_watermark = Button(text='Confirm watermark ', command=watermark_text_button_clicked)
user_watermark.grid(column=2,row=3)

add_watermark = Button(text='Show updated picture', command=edit_user_image)
add_watermark.grid(column=2,row=4)




window.mainloop()

