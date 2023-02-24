import tkinter #for functionality
import customtkinter #Just for better appearance
from pytube import YouTube
from pytubemp3 import YouTube as ytmp3 #Not used

def startDownload(index):
    try:
        progressBar.set(0)
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        print(index)
        if index == 0 :
            video = ytObject.streams.get_highest_resolution()
        else :
            video = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title,text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download Complete")
    except:
        finishLabel.configure(text="Download error : Invalid Link", text_color="red")
    
    
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-bytes_remaining
    percentage_of_complition = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_complition))
    pPercentage.configure(text = per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_of_complition/100))


#System Default
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")
#app.iconbitmap("appIcon.ico")

frame_1 = customtkinter.CTkFrame(master=app, corner_radius=20)
frame_1.pack(pady=20, padx=10, fill="x", expand=True,)

#UI Elements
title = customtkinter.CTkLabel(master=frame_1, text = "Insert a Youtube link")
title.pack(padx=10,pady = 10)

url_variable = tkinter.StringVar()
link = customtkinter.CTkEntry(master=frame_1, width = 350, height = 40,textvariable = url_variable)
link.pack()

finishLabel = customtkinter.CTkLabel(master=frame_1, text="")
finishLabel.pack()

#progess percent
pPercentage = customtkinter.CTkLabel(master=frame_1,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(master=frame_1, width = 450)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

#In this frame i wont use pack() at all so i can use the grid layout!
buttonsFrame = customtkinter.CTkFrame(master=frame_1,fg_color="#302c2c")
buttonsFrame.pack(padx=10,pady=10,fill="none",expand=False)

downloadBtn = customtkinter.CTkButton(master=buttonsFrame, text="Download", command = lambda: startDownload(0), fg_color="#3f97db",hover_color="#1f6aa4",height=50)
#downloadBtn.pack(padx = 10,pady = 10,side=tkinter.LEFT,anchor="c")
downloadBtn.grid(padx=(0,10),row=0,column=0)


downloadAudioOnlyBtn = customtkinter.CTkButton(master=buttonsFrame, text="Download Audio Only", command= lambda: startDownload(1), fg_color="#3f97db",hover_color="#1f6aa4",height=50)
#downloadAudioOnlyBtn.pack(padx = 10,pady = 10,anchor="c")
downloadAudioOnlyBtn.grid(padx=(10,0),row=0,column=1) #Single Sided padding


#canvas = customtkinter.CTkCanvas(app, width = 720, height= 10, bg = "#3f97db")
#canvas.pack()

#canvas.create_line(0,5,720,5,fill="#1b39d3",width=20)


#Run app as Loop so it doesnt close instantly
app.mainloop()