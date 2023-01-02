#!/usr/bin/env python3
from tkinter import *
from tkinter.filedialog import asksaveasfile
from pytube import YouTube
from PIL import ImageTk,Image
import os
import cv2

def run():


    def get_vid(link):
        if not link: return
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()            

    #main window
    window = Tk()
    window.resizable(0,0)
    window.config(background='black')
    window.geometry('600x600')
    window.title('YouLoad')


    #loading logo
    logo = Image.open('assets/Color-YouTube-logo.jpg')
    logo = logo.resize((300,200),Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    #label for containing youtube logo
    holder = Label(image=logo,bd= 0)
    holder.place(x = 155 , y = 100)
    
    cap = Label(text = 'Instant Video Downloader',fg = 'white',bg = 'black',font = ('',20))
    cap.place(x=132,y=275)

    prompt = Label(text = 'Enter URL:',fg = 'white',bg = 'black',font = ('',13))
    prompt.place(x=80,y=340)

    field = Entry(bg='#6e6e73',bd=0,insertbackground='black',width = 30,font = ('',13) )
    field.place(x= 180,y=340)

    download = Button(relief=FLAT,text='Download',font=('',19),bg='#9da6ab',fg = 'black')
    download.place(x=225,y=400)
    download.config(command = lambda: get_vid(field.get()))    

    window.mainloop()

def test():
    test= open('The World is still Beautiful.mp4')
    print(test.read())

if __name__ == '__main__':
    #test()
    run()