# importing tkinter
from tkinter import *
# importing YouTube module
from pytube import YouTube
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x250")
# setting the title of the GUI
root.title("Youtube video downloader application")
# defining download function
def download():
    # using try and except to execute program without errors
    try:
        myVar.set("Descargando...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video descargado exitosamente")
    except Exception as e:
        myVar.set("ERROR")
        root.update()
        link.set("Ingresa el link correcto")

# created the Label widget to welcome user
Label(root, text="Bienvenido a youtube\nDownloader Application", font="Consolas 15 bold").pack()
# declaring StringVar type variable
myVar = StringVar()
# setting the default text to myVar
myVar.set("Ingresa el link debajo")
# created the Entry widget to ask user to enter the url
Entry(root, textvariable=myVar, width=40).pack(pady=10)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)
# created and called the download function to download video
Button(root, text="Descargar video", command=download).pack()
# running the mainloop
root.mainloop()