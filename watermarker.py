from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import os

class WatermarkApp:
    def __init__(self):
        self.wm_path = os.getenv("watermark_path")
    
        self.canvas = Canvas(width=600, height=400, bg="white")
        self.text = self.canvas.create_text(300, 200, text="Upload your image", font=("Courier", 12, "italic"))
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.canvas.image = []

        #button
        self.upload = Button(text="Upload", command=self.upload_img, padx=10, pady=20)
        self.upload.grid(column=0, row=1)
        self.watermark = Button(text="Watermark", command=self.watermark_img, padx=10, pady=20)
        self.watermark.grid(column=1, row=1)
        self.save = Button(text="Save", command=self.save_img, padx=10, pady=20)
        self.save.grid(column=2, row=1)

    def upload_img(self):
        img_path1 = filedialog.askopenfilename(title="Select the first image")
        if img_path1: 
            self.canvas.delete("all")
            img = Image.open(img_path1)
            img.thumbnail((500, 500))
            img_tk = ImageTk.PhotoImage(img)
            self.canvas.config(width=img.width, height=img.height)
            self.canvas.create_image(img.width / 2, img.height / 2, image=img_tk)
            self.canvas.image.append(img_tk)

    def watermark_img(self):
        wm = Image.open(self.wm_path)
        wm.thumbnail((50, 50))
        wm_tk = ImageTk.PhotoImage(wm)
        self.canvas.create_image(self.canvas.winfo_width()-60, self.canvas.winfo_height()-60, anchor='nw', image=wm_tk)
        self.canvas.image.append(wm_tk)

    def save_img(self):
        self.canvas.postscript(file="image.ps", colormode='color', pagewidth=self.canvas.winfo_width() * 3, pageheight=self.canvas.winfo_height() * 3)
        final_img = Image.open("image.ps")
        final_img.save("image.png", format="png")

if __name__ == "__main__":
    window = Tk()
    window.config(padx=50, pady=50)
    window.title("Watermark Stamp")
    app = WatermarkApp()
    window.mainloop()