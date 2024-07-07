import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle
import pyglet

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reproductor de Música")
        self.root.geometry("400x250")

        self.style = ThemedStyle(self.root)  
        self.style.set_theme("clam")

        self.music = None
        self.player = None
        self.playing = False

        self.open_button = tk.Button(self.root, text="Abrir archivo", command=self.open_file)
        self.open_button.pack(padx=20, pady=10)

        self.play_button = tk.Button(self.root, text="Play", state=tk.DISABLED, command=self.play)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pausar", state=tk.DISABLED, command=self.pause)
        self.pause_button.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progress_bar.pack(pady=5)

        self.close_button = tk.Button(self.root, text="Cerrar", command=self.close)
        self.close_button.pack(pady=10)

        self.update_progress_bar()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.playing = False
            self.music = pyglet.media.load(file_path)
            self.player = pyglet.media.Player()
            self.progress_bar.config(value=0)
            self.update_progress_bar()

    def play(self):
        if self.music and not self.playing:
            self.player.queue(self.music)
            self.player.play()
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.playing = True

    def pause(self):
        if self.playing:
            self.player.pause()
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.playing = False

    def update_progress_bar(self):
        if self.playing and self.music:
            position = self.player.time
            duration = self.music.duration
            progress = (position / duration) * 100
            self.progress_bar.config(value=progress)
        self.root.after(100, self.update_progress_bar)

    def close(self):
        if self.playing:
            self.player.pause()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
