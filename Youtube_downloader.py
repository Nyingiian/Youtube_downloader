from pytube import YouTube
from playsound import playsound
import tkinter as tk

""" Variable for the width, height, click sound"""

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 150
WINDOW_TITLE = "Youtube Downloader"
BUTTON_CLICK_SOUND = "clicks.m4a"


class YoutubeDownloader:
    def __init__(self):
     #when you're using an object oriented structure you need to initialize
        self.window = tk.Tk()
        self.geometry = ("{}*{}".format(WINDOW_HEIGHT,WINDOW_WIDTH))
        self.window.configure(bg="#2b5480")  #color 
        self.window.title(WINDOW_TITLE)
        
        #Creating labels
        self.link_label = tk.Label(self.window, text = "Download link")
        self.link_label.grid(column = 0, row = 0)
        self.name_label = tk.Label(self.window, text = "Save file as")
        self.name_label.grid(column = 0, row = 1)
        self.path_label = tk.Label(self.window, text = "Save file path")
        self.path_label.grid(column = 0, row = 2)
        self.ext_label = tk.Label(self.window, text = "File extension")
        self.ext_label.grid(column = 0, row = 3)
        

        #create entry

        #specifying the position where the entry should be

        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 0)
        self.name_entry = tk.Entry(master= self.window, width = 40)
        self.name_entry.grid(column = 1, row = 1)
        self.path_entry = tk.Entry(master= self.window, width = 40)
        self.path_entry.grid(column = 1, row = 2)
        self.ext_entry = tk.Entry(master= self.window, width = 40)
        self.ext_entry.grid(column = 1, row = 3)

        #Create download button (dummy function)
        self.download_button = tk.Button(self.window, text = "Download", command = self.__get_link)
        self.download_button.grid(column = 1, row = 4)

        return

    #private function starts double underscore
    # the private function means that it's only going to be called within class
    def __downloader(self,link,save_path = "", save_name = "", extension = "mp4"):

        #create a youtube object
        yt = YouTube(link)
        yt_stream = yt.stream.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()
        #filtered based on setting paramaters
        yt_stream.download(output_path = save_path, filename = save_name)

        return


    def __get_link(self):
        playsound = BUTTON_CLICK_SOUND
        link = self.link_entry.get()
        path = self.path_entry.get()    
        name = self.name_entry.get()
        ext = self.ext_entry.get()

        self.__downloader(link, path, name, ext)

        return


    def run_app(self):
        self.window.mainloop()
        return

#with object oriented, you should create an instance the class
 
        

if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run_app()



    
