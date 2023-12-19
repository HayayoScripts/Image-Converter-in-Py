import os
from tkinter import Tk, Label, Button, filedialog, StringVar, Menubutton, Menu
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter")
        master.geometry("400x400")
        master.resizable(False, False)

        self.heading_label = Label(master, text="Image Converter", font=("Inria Sans", 25, "bold"), bg="black", fg="white")
        self.heading_label.place(y=32, x=69)

        self.label = Label(master, text="Selected image:", bg="black", fg="white", justify="center", font=("Inria Sans", 10, "bold"))
        self.label.pack()
        
        self.select_image_button_img = Image.open(r"Selection Area.png")
        self.select_image_button_img = ImageTk.PhotoImage(self.select_image_button_img)

        self.select_button = Button(master, image=self.select_image_button_img, command=self.select_image, bg="black", relief="flat")  # Select Image
        self.select_button.image = self.select_image_button_img
        self.select_button.place(y=89, x=40)

        self.convert_button_img = Image.open(r"Convert.png")
        self.convert_button_img.thumbnail((100, 50))
        self.convert_button_img = ImageTk.PhotoImage(self.convert_button_img)

        self.convert_button = Button(master, image=self.convert_button_img, command=self.convert_image, bg="black", relief="flat")  # Convert
        self.convert_button.image = self.convert_button_img
        self.convert_button.place(y=323, x=135)

        self.Convert_to_label = Label(master, text="Convert To:", font=("Inria Sans", 13, "bold"), bg="black", fg="white")
        self.Convert_to_label.place(y=207, x=102)

        self.format_var = StringVar(master)
        self.format_var.set("Select")

        self.dropdown_select_button_img = Image.open(r"Convert Options.png")
        self.dropdown_select_button_img = ImageTk.PhotoImage(self.dropdown_select_button_img)

        self.format_dropdown_button = Menubutton(master, image=self.dropdown_select_button_img, compound="right", font=("Circular", 13), bg="black", fg="white", relief="flat",  borderwidth=0, highlightthickness=0)  
        self.format_dropdown_button.place(y=200, x=209)

        self.format_dropdown_menu = Menu(self.format_dropdown_button, tearoff=0)

        self.format_dropdown_menu.add_radiobutton(label="JPG", variable=self.format_var, value="JPG", background='#6271FB',foreground='white')
        self.format_dropdown_menu.add_radiobutton(label="PNG", variable=self.format_var, value="PNG", background='#6271FB',foreground='white')
        self.format_dropdown_menu.add_radiobutton(label="JPEG", variable=self.format_var, value="JPEG", background='#6271FB',foreground='white')
        self.format_dropdown_menu.add_radiobutton(label="WebP", variable=self.format_var, value="WebP", background='#6271FB',foreground='white')

        self.format_dropdown_button.config(menu=self.format_dropdown_menu, relief="flat", bg="black",bd=0, borderwidth=0, highlightthickness=0)


    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.webp")])

        if file_path:
            self.label.config(text=f"Selected image:\n{file_path}")

    def convert_image(self):
        selected_image = self.label.cget("text")[16:]  # image path

        if selected_image:
            try:
                image = Image.open(selected_image)
                current_format = image.format.lower()

                new_format = self.format_var.get().lower()  # format select

                new_file_path = os.path.splitext(selected_image)[0] + f".{new_format}"  # new

                image.save(new_file_path, format=new_format)  # save

                print(f"Conversion successful! Image saved as: {new_file_path}")

            except Exception as e:
                print(f"Error converting image: {e}")
        else:
            print("No image selected.")

if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.configure(bg="black")
    root.mainloop()
