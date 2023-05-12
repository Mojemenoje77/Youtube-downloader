import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from validators import url as valid_url

def download_video():
    video_url = url_entry.get()
    if not valid_url(video_url) or "youtube" not in video_url:
        status_label.config(text="Neplatná URL adresa videa!")
        return

    try:
        yt = YouTube(video_url)
        selected_format = format_choice.get()
        if selected_format == "mp4":
            video = yt.streams.get_highest_resolution()
        elif selected_format == "mp3":
            video = yt.streams.filter(only_audio=True).first()
        else:
            return
        
        output_path = filedialog.askdirectory()  # Let user choose output directory
        video.download(output_path)
        status_label.config(text="Video bylo staženo!")
    except Exception as e:
        status_label.config(text="Chyba při stahování videa: " + str(e))

window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("400x150")
window.config(bg="#830808", highlightbackground="#DAA57C", highlightthickness=4)
window.minsize(width=300, height=300)
window.resizable(False,False)

background_label = tk.Label(window, text="YD", font=("Georgia", 90), fg="#DAA57C", bg="#830808")
background_label.place(x=127, y=120)

background_label = tk.Label(window, text="Youtube downloader", font=("Georgia", 8), fg="#DAA57C", bg="#830808")
background_label.place(x=127, y=200)

background_label = tk.Label(window, text="\u21E9", font=("Georgia", 40), fg="#DAA57C", bg="#830808")
background_label.place(x=84, y=185)

url_entry = tk.Entry(window, width="40")
url_entry.pack(pady=5)
url_entry.config(highlightbackground="#DAA57C", highlightcolor="#DAA57C", highlightthickness=3)

format_choice = tk.StringVar(window)
format_choice.set("mp4")  # Default format

format_menu = tk.OptionMenu(window, format_choice, "mp4", "mp3", "avi", "flv")  # More formats
format_menu.config(bg= "#82634A", font="Georgia", highlightbackground="#DAA57C", highlightcolor="#DAA57C", highlightthickness=2 )
format_menu.pack()

download_button = tk.Button(window, text="Stáhnout", command=download_video, width="15", background= "#82634A", font="Georgia")
download_button.pack(pady=4)
download_button.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)

status_label = tk.Label(window, text="", width="15")
status_label.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
status_label.pack(pady=3)

window.mainloop()


#Vytvořil : Filip Mazúr
#Autorstvo :Filip Mazúr 