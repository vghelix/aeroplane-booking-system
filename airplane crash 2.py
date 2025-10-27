import customtkinter as c
from tkinter import messagebox
from PIL import ImageTk, Image

def login():
    swiss = c.CTk()
    swiss.geometry("560x560")
    nam = c.CTkLabel(swiss, text="enter you name ")
    nam.pack()
    name = c.CTkEntry(swiss)
    name.pack()
    passw = c.CTkLabel(swiss, text="Enter your password")
    passw.pack()
    passwe = c.CTkEntry(swiss)
    passwe.pack()

    def ticketbooking():
        window = c.CTk()
        window.geometry("340x340")
        label = c.CTkLabel(window, text="welcome to ethihad")
        label.pack()
        window.config(background="black")
        n = c.CTkLabel(window, text='YOUR NAME:')
        n.pack()
        ne = c.CTkEntry(window)
        ne.pack()
        p = c.CTkLabel(window, text="enter the passport no:")
        p.pack()
        pe = c.CTkEntry(window)
        pe.pack()
        la = c.CTkLabel(window, text="enter the destination")
        la.pack()
        lae = c.CTkEntry(window)
        lae.pack()
        name = ne.get()
        passport = pe.get()
        destination = lae.get()
        window.mainloop()

        def click():
            import csv
            with open("Airways.csv", "a") as f:
                x = csv.writer(f)
                x.writerow([name, passport, destination])
                messagebox.showinfo(message="details added")
        button = c.CTkButton(window, text="NEXT>", command=click)
        button.pack()

    def destroy():
        root = c.CTk()
        root.geometry("560x560")
        root.title("ticket")
        l = c.CTkLabel(root, text="HERE IS YOUR TICKET")
        l.pack()
        img = ImageTk.PhotoImage(Image.open("C:/Users/preet/OneDrive/Desktop/project 12/plane ticket2.jpg"),
                                 size=(360, 360))
        img_label = c.CTkLabel(root, image=img)
        img_label.pack()

        root.mainloop()

    buttone = c.CTkButton(swiss, text="continue>", command=destroy)
    buttone.pack()
    def subclick():
        with open('Airways.csv', 'r') as file:
            import csv
            r = csv.reader(file)
            l = list(r)
        c = False
        username = name.get()
        password = passwe.get()
        for i in range(len(l)):
            if l[i][0] == username:

                if password == l[i][1]:
                    print('_________')
                    print("login sucessfully")
                    print('_________')
                    messagebox.showinfo(message="IDENTITY CONFIRMED")
                    nextpage = c.CtkButton(swiss, text="clik to continue to booking", command=ticketbooking)
                    nextpage.pack()
                else:
                    messagebox.showinfo(message="wrong")
                    swiss.destroy()
    b3=c.CTkButton(swiss,text="submit",command=subclick)
    b3.pack()


    swiss.mainloop()




def signup():
    def win():
        sign.destroy()
        window = c.CTk()
        window.geometry("340x340")
        label = c.CTkLabel(window, text="welcome to ethihad")
        label.pack()
        window.config(background="black")
        n = c.CTkLabel(window, text='YOUR NAME:')
        n.pack()
        ne = c.CTkEntry(window)
        ne.pack()
        p = c.CTkLabel(window, text="enter the passport no:")
        p.pack()
        pe = c.CTkEntry(window)
        pe.pack()
        la = c.CTkLabel(window, text="enter the destination")
        la.pack()
        lae = c.CTkEntry(window)
        lae.pack()
        name = ne.get()
        passport = pe.get()
        destination = lae.get()

        def click():
            import csv
            with open("plane2.csv", "a") as f:
                x = csv.writer(f)
                x.writerow([name, passport, destination])
                messagebox.showinfo(message="details added")
        button = c.CTkButton(window, text="NEXT>", command=click)
        button.pack()

        window.mainloop()

        def destroy():
            root = c.CTk()
            root.geometry("560x560")
            root.title("ticket")
            l = c.CTkLabel(root, text="HERE IS YOUR TICKET")
            l.pack()
            img = ImageTk.PhotoImage(Image.open("C:/Users/preet/OneDrive/Desktop/project 12/plane ticket2.jpg"),
                                     size=(360, 360))
            img_label = c.CTkLabel(root, image=img)
            img_label.pack()

            root.mainloop()

        buttone = c.CTkButton(window, text="continue>", command=destroy)
        buttone.pack()

    def subeclick():
        import csv
        with open('Airways.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            username = sname.get()
            password = apass.get()
            while True:
                checkpass = checke.get()
                if password == checkpass:
                    writer.writerow([username, password])
                    print('_____________')
                    print('Signed up/Account created succesfully')
                    print('_____________')
                    messagebox.showinfo(message="confirmed")
                    winner = c.CTkButton(sign, text="NEXT>", command=win)
                    winner.pack()
                    break
                else:
                    print('Incorrect Password')
                    messagebox.showinfo(message="incorrect password")
                    sign.destroy()
    menu.destroy()
    sign = c.CTk()
    sign.geometry("360x360")
    sign.title("SIGNUP")
    l4 = c.CTkLabel(sign, text="ENTER YOUR NAME")
    l4.pack()
    sname = c.CTkEntry(sign)
    sname.pack()
    l5 = c.CTkLabel(sign, text="enter your password")
    l5.pack()
    apass = c.CTkEntry(sign)
    apass.pack()
    check = c.CTkLabel(sign, text="enter your password again")
    check.pack()
    checke = c.CTkEntry(sign)
    checke.pack()
    bo = c.CTkButton(sign, text="SUBMIT", command=subeclick)
    bo.pack()

    sign.mainloop()





menu=c.CTk()
menu.geometry("550x450")
menu.title("MENU")
img= ImageTk.PhotoImage(Image.open("C:/Users/preet/OneDrive/Desktop/hello/airplane photo.jpg"),size=(360,360))
img_label= c.CTkLabel(menu,image=img)
img_label.pack()
label1=c.CTkLabel(menu,text="login").pack()
b=c.CTkButton(menu,text="NEXT>",command=login)
b.pack()
label2=c.CTkLabel(menu,text="signup")
label2.pack()
bt=c.CTkButton(menu,text="NEXT>",command=signup)
bt.pack()
menu.mainloop()
