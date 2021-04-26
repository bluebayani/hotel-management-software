import tkinter as tk
import os
import shutil
import random
import string
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageOps
from guest import Guest
from guest_manager import *


class CapabilityFive:
    def __init__(self, frame, index):
        self.frame = frame
        # item in guest
        # self.guest[0].get_fname()
        self.guest = get_guests()
        self.index = index
        self.filename = self.guest[index].get_img_path()
        profile_title = tk.Label(
            self.frame, text="Guest Profile", font=("Times", 20, "bold"))
        profile_title.grid(row=0, column=0)
        btn = Button(self.frame, text='replace image',
                     command=self.replace_img).grid(row=2, column=0)
        save_btn = tk.Button(self.frame, text="Save All Changes", command=self.save_changes, anchor=tk.W,
                             width=20).grid(row=10, column=1, pady=5)

        # create the labels for each field
        fname_label = tk.Label(self.frame, text="First Name",
                               anchor='w', width=20).grid(row=3, column=0, padx=15, pady=5)
        lname_label = tk.Label(self.frame, text="Last Name", anchor='w',
                               width=20).grid(row=4, column=0, padx=15, pady=5)
        phone_label = tk.Label(self.frame, text="Phone Number",
                               anchor='w', width=20).grid(row=5, column=0, padx=15, pady=5)
        address_label = tk.Label(self.frame, text="Address",
                                 anchor='w', width=20).grid(row=6, column=0, padx=15, pady=5)
        email_label = tk.Label(self.frame, text="E-mail", anchor='w',
                               width=20).grid(row=7, column=0, padx=15, pady=5)
        id_label = tk.Label(self.frame, text="ID", anchor='w',
                            width=20).grid(row=8, column=0, padx=15, pady=5)
        vehicle_label = tk.Label(self.frame, text="Vehicle License Plate",
                                 anchor='w', width=20).grid(row=9, column=0, padx=15, pady=5)

        # create the fields
        self.fname_field = tk.Entry(self.frame)
        self.fname_field.grid(row=3, column=1, padx=15, pady=5)
        self.lname_field = tk.Entry(self.frame)
        self.lname_field.grid(row=4, column=1, padx=15, pady=5)
        self.phone_field = tk.Entry(self.frame)
        self.phone_field.grid(row=5, column=1, padx=15, pady=5)
        self.address_field = tk.Entry(self.frame)
        self.address_field.grid(row=6, column=1, padx=15, pady=5)
        self.email_field = tk.Entry(self.frame)
        self.email_field.grid(row=7, column=1, padx=15, pady=5)
        self.id_field = tk.Entry(self.frame)
        self.id_field.grid(row=8, column=1, padx=15, pady=5)
        self.vehicle_field = tk.Entry(self.frame)
        self.vehicle_field.grid(row=9, column=1, padx=15, pady=5)
        self.populate_fields()

    def open_fn(self):
        # choose file from computer and save it to the projects res folder.
        self.filename = filedialog.askopenfilename(title='open')
        if self.filename == "":
            self.filename = self.guest[self.index].get_img_path()
        return self.filename

    def save_img(self):
        # if file not in folder save the file to the res folder
        fn = os.path.basename(self.filename)
        file_path = os.path.join(r"./res/", fn)
        self.img = Image.open(self.filename)
        self.img = self.img.resize((250, 250), Image.ANTIALIAS)
        self.img.save(file_path, 'JPEG')
        saved_fn = "./res/" + fn
        return saved_fn

    def replace_img(self):
        # replaces old image with new image
        self.x = self.open_fn()
        self.new_img = Image.open(self.x)
        self.new_img = self.new_img.resize((250, 250), Image.ANTIALIAS)
        self.new_img = ImageTk.PhotoImage(self.new_img)
        self.panel.configure(image=self.new_img)
        self.panel.image = self.new_img

    def populate_img(self, path):
        self.img = Image.open(path)
        self.img = self.img.resize((250, 250), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.frame, image=self.img)
        self.panel.image = self.img
        self.panel.grid(row=1, column=0, padx=15, pady=5)

    # EXAMPLE: pass in self.guest[0]
    def populate_fields(self):
        self.fname_field.insert(0, self.guest[self.index].get_fname())
        self.lname_field.insert(0, self.guest[self.index].get_lname())
        self.phone_field.insert(0, self.guest[self.index].get_phone())
        self.address_field.insert(0, self.guest[self.index].get_address())
        self.email_field.insert(0, self.guest[self.index].get_email())
        self.id_field.insert(0, self.guest[self.index].get_id())
        self.vehicle_field.insert(0, self.guest[self.index].get_vehicle())
        self.populate_img(self.guest[self.index].get_img_path())

    def save_changes(self):
        fn = os.path.basename(self.filename)
        file_path = os.path.join(r"./res/", fn)

        if not os.path.exists(file_path):
            self.filename = self.save_img()
        changed_fields = [self.fname_field.get(), self.lname_field.get(), self.phone_field.get(), self.address_field.get(),
                          self.email_field.get(), self.id_field.get(), self.vehicle_field.get(), self.filename]
        print("changes saved...")
        save_label = tk.Label(
            self.frame, text="Changes saved to database.").grid(row=11, column=0, padx=15, pady=5)
        update_guest(self.index, changed_fields)
