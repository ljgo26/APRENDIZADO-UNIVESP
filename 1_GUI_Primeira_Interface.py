from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='../img_botão.gif').subsample(1)
img = Label(master=root, image=photo)
img.pack(side=TOP)
texto_img = Label(master=root, font='Arial', text='Minha primeira interface')
texto_img.pack(side=BOTTOM)
root.mainloop()
