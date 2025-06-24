
from tkinter import *
import yt_dlp

import os

# Add ffmpeg path to system PATH (for yt-dlp to use)
ffmpeg_path = os.path.abspath("ffmpeg/bin")
os.environ["PATH"] += os.pathsep + ffmpeg_path


def download():
    url = link.get('1.0', 'end').strip()
    root.title('Downloading....')

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            Label(root, text=f"✅ Downloaded: {info.get('title')}", fg="green").place(x=10, y=190)
            root.title('Success')

    except Exception as e:
        Label(root, text=f"❌ Error: {e}", fg="red").place(x=10, y=190)


root = Tk()

root.title('You Tube Video downloader')
root.geometry('400x250')


img = PhotoImage(file='youtube.png')
Label(image=img, bd=1).place(x=150,y=28)

Label(root, text='Paste Link: ').place(x=4, y=58)

link = Text(root, fg='black', bd=1, height=4, width=38, bg='light yellow')
link.place(x=80, y=58)

btn = Button(root, width=8, padx=1, pady=3, text='Download', command = download , bg='pink', fg='black', border=1)
btn.place(x=190, y=150)


root.mainloop()