from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import pygame
index=0
listofsongs=[]
#window
window=Tk()
window.title("MUSIC_PLAYEH")
window.geometry('700x600')
window.iconbitmap(r'D:\\music_player\\icon.ico')

lbl=Label(text="MUSIC_PLAYER",font=("Arial Bold",50))
lbl.place(x=100,y=30)

def fun():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    f=window.filename
    listofsongs.append(f)
    '''f_lst=Listbox(window)
    f_lst.place(x=60,y=300)'''
    f_lst.insert(END,listofsongs)

def info():
    messagebox.showinfo("about","developed by - himanshu chaudhary")


#menu
menubar=Menu(window)
menubar.add_command(label="ADD  SONG",command=fun)
menubar.add_command(label="ABOUT",command=info)
menubar.add_command(label="QUIT",command=quit)
window.config(menu=menubar)

#import photo
photo_icon=PhotoImage(file=r'D:\\music_player\\icon.png')
photo_playbtn=PhotoImage(file=r'D:\\music_player\\playbtn.png')
photo_pausebtn=PhotoImage(file=r'D:\\music_player\\pause.png')
photo_stopbtn=PhotoImage(file=r'D:\\music_player\\btn-grey-play-stop-512.png')
photo_next=PhotoImage(file=r'D:\\music_player\\9.5-512.png')
photo_prev=PhotoImage(file=r'D:\\music_player\\9.5-512 - Copy.png')
pygame.init()



def play():
    pygame.mixer.music.load(listofsongs[index]) #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def stop():
    pygame.mixer.music.stop()
def set_vol(val):
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)
def nxt():
    pygame.mixer.music.load(listofsongs[index+1])
    pygame.mixer.music.play()
def pre():
    pygame.mixer.music.load(listofsongs[index-2])
    pygame.mixer.music.play()



ico=Button(image=photo_icon,command=play)
ico.place(x=225,y=125)

pausebtn=Button(window,image=photo_pausebtn,command=pause)
pausebtn.place(x=225,y=400)

unpausebtn=Button(window,image=photo_playbtn,command=unpause)
unpausebtn.place(x=310,y=400)

stopbtn=Button(window,image=photo_stopbtn,command=stop)
stopbtn.place(x=400,y=400)

scale=Scale(window,from_=100,to=0,command=set_vol)
scale.set(70)
pygame.mixer.music.set_volume(70)
scale.place(x=590,y=355)

nxtbtn=Button(window,image=photo_next,command=nxt)
nxtbtn.place(x=470,y=200)

prebtn=Button(window,image=photo_prev,command=pre)
prebtn.place(x=150,y=200)

f_lst=Listbox(window)
f_lst.place(x=60,y=300)
#f_lst.insert(END,listofsongs)


window.mainloop()
