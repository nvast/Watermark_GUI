from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Watermarker")
window.config(padx=200, pady=100, bg="#B6D5E1")

watermark_color = (255, 255, 255, 127)

# ---------------- FUNCTIONALITY ---------------- #

def search_file():
    filename = filedialog.askopenfilename(initialdir='C:/Users/MyName/Desktop/', title='Select an image')
    return filename

def add_watermark(image):
    open_image = Image.open(image).convert("RGBA")
    image_width, image_height = open_image.size
    draw = ImageDraw.Draw(open_image)

    text = simpledialog.askstring("Watermark text", "Enter watermark text")
    font_size = int(image_width / 30)
    font = ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width * 30 / 31), int(image_height * 30 / 31)

    draw.text((x, y), text, font=font, fill=watermark_color, anchor='rs')

    open_image.show()
    open_image.save(filedialog.asksaveasfilename(initialdir='C:/Users/MyName/Desktop/', title='Save image', defaultextension=".png"))

# ---------------- CANVAS ---------------- #

canvas = Canvas(width=250, height=250, bg="#E2EFF1", highlightthickness=0)
photo_icon = PhotoImage(file="photo_icon.png")
canvas.create_image(125, 125, image=photo_icon)
canvas.grid(column=0, row=0)

# ---------------- SPACER ---------------- #

space_row = Frame(window, height=50, bg="#B6D5E1")
space_row.grid(column=0, row=1)

# ---------------- BUTTON ---------------- #

upload_button = Button(text="Upload image", command=lambda: add_watermark(search_file()), bg="#E2EFF1")
upload_button.grid(column=0, row=2)

window.mainloop()

