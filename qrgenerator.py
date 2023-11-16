import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    link = link_entry.get()
    if link:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((200, 200))  # Resize the image
        qr_image = ImageTk.PhotoImage(image=img)
        qr_label.config(image=qr_image)
        qr_label.image = qr_image
        qr_label.pack(pady=(0, 10))  # Adjust the padding between QR code and window edge
    else:
        messagebox.showerror("Error", "Please enter a link!")
def rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
        x1 + radius, y1,
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)
def on_button_click(event):
    generate_qr()
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x300")
link_label = tk.Label(root, text="Enter a Link:", font=("Arial", 12, "underline bold"))
link_label.pack(pady=5)
link_entry = tk.Entry(root, width=40, font=("Arial", 10))
link_entry.pack(pady=5)
canvas = tk.Canvas(root, width=200, height=40, highlightthickness=0)
canvas.pack(pady=5)
button_shape = rounded_rect(canvas, 0, 0, 200, 40, radius=15, fill="black")
canvas.bind('<Button-1>', on_button_click)
canvas.create_text(100, 20, text="Generate QR Code", fill="white", font=("Arial", 10, "bold"))
qr_label = tk.Label(root)
qr_label.pack()
qr_label.pack(pady=(0, 10))
root.mainloop()
