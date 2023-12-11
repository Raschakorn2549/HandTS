import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()

root.config(bg='light blue')
root.title('Translate App')

main_frame = Frame(root)
main_frame.grid()
main_frame.config(bg='light blue')
main_frame.place(in_=root, anchor="c", relx=.5, rely=.5)

title_label = Label(main_frame,bg="light blue", font="Times 36", text="Hand Translate Program")
title_label.grid(row=0, column=0, columnspan=2)
description_label = Label(main_frame,bg="light blue", font="Times 18", text="By SMTE Surawittayakarn School")
description_label.grid(row=1, column=0, columnspan=2, pady=10)

left_frame = Frame(main_frame)
left_frame.grid(row=2, column=0)

right_frame = Frame(main_frame)
right_frame.grid(row=2, column=1, padx=50)
right_frame.config(bg='light blue')

camera_label = Label(left_frame)
camera_label.grid(row=0, column=0)

translate_label = Label(left_frame, font='Times 24')
translate_label.grid(row=1, column=0)

translate_button_label = Label(right_frame, text = "Translate Menu")
translate_button_label.config(font='Times 24')
translate_button_label.grid(row=0, column=0, columnspan=2, pady=30, sticky=N, ipadx=5, ipady=5)

def createPictureLabel():
    global picture_label
    picture_label = Label(left_frame)
    picture_label.grid(row=0, column=0)

def openNewWindowsad():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/sad.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowsick():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/sick.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowclever():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/clever.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowcute():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/cute.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowthanku():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/thanku.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindownoproblem():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/noproblem.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowbeauty():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/beautiful.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowhungry():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/hungry.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowfull():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/full.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def openNewWindowmissu():
    createPictureLabel()
    phototk = ImageTk.PhotoImage(image = Image.open("Asset/missu.jpg"))
    picture_label.phototk = phototk
    picture_label.configure(image=phototk)
    picture_label.after(2000, picture_label.destroy)

def textbox():
    b1 = Button(right_frame, text = "Sad",width=15, height=3, command = openNewWindowsad )
    b2 = Button(right_frame, text = "Sick",width=15, height=3, command = openNewWindowsick )
    b3 = Button(right_frame, text = "Clever",width=15, height=3, command = openNewWindowclever )
    b4 = Button(right_frame, text = "Cute",width=15, height=3, command = openNewWindowcute )
    b5 = Button(right_frame, text = "Thank you",width=15, height=3, command = openNewWindowthanku )
    b6 = Button(right_frame, text = "No Problem",width=15, height=3, command = openNewWindownoproblem )
    b7 = Button(right_frame, text = "Beautiful",width=15, height=3, command = openNewWindowbeauty )
    b8 = Button(right_frame, text = "Hungry",width=15, height=3, command = openNewWindowhungry )
    b9 = Button(right_frame, text = "Full",width=15, height=3, command = openNewWindowfull )
    b10 = Button(right_frame, text = "Miss you",width=15, height=3, command = openNewWindowmissu )
    exit_button = Button(right_frame, text = "Exit",width=15, height=3, command = root.destroy)

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=2, column=0)
    b4.grid(row=2, column=1)
    b5.grid(row=3, column=0)
    b6.grid(row=3, column=1)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=5, column=0)
    b10.grid(row=5, column=1)
    exit_button.grid(row=6, column=0, columnspan=2, pady=30, sticky=S)

classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["Sad", "Sick", "Clever,Intelligent", "Cute", "Thank you",
           "No problem", "Beautiful", "Hungry", "Full", "Miss you"]

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300

def translate_func():
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal)) 
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        cv2.rectangle(imgOutput, (x - offset, y - offset-50),
                      (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        translate_label.configure(text=labels[index], fg="black")
        cv2.rectangle(imgOutput, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)
        
    else:
        translate_label.configure(text=" - Finding Hand - ", fg="red")
    
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    imgcv = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image = imgcv)
    camera_label.imgtk = imgtk
    camera_label.configure(image=imgtk)
    camera_label.after(20, translate_func)
    cv2.waitKey(1)

root.attributes('-fullscreen', True)

textbox()
translate_func()

root.mainloop()

#Surawittayakarn School
#For SMTE Project
#By 6/1 Student (8,24)
