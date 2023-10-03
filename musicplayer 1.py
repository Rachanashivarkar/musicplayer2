import os
import pygame
from tkinter import *
from tkinter import filedialog

# Initialize pygame
pygame.mixer.init()

# Create a Tkinter window
root = Tk()
root.title("Music Player")
root.geometry("400x200")

# Create a function to open a file dialog and select music
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Create GUI elements
frame = Frame(root)
frame.pack(pady=20)

open_button = Button(frame, text="Open Music File", command=open_file)
open_button.pack(padx=20)

play_button = Button(frame, text="Play", command=lambda: pygame.mixer.music.unpause())
play_button.pack(pady=10)

pause_button = Button(frame, text="Pause", command=pygame.mixer.music.pause)
pause_button.pack()

stop_button = Button(frame, text="Stop", command=pygame.mixer.music.stop)
stop_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
