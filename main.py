import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


def download_video():
    url = entry.get()
    if url:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        path = filedialog.asksaveasfilename(defaultextension=".mp4")
        if path:
            video.download(path)
            label.config(text="Video downloaded successfully")
        else:
            label.config(text="Failed to download video")
    else:
        label.config(text="Enter a valid YouTube URL")


root = tk.Tk()
root.title("YouTube Video Downloader")

label = tk.Label(root, text="Enter the YouTube video URL:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=10)

root.mainloop()
