from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import os
import subprocess

bookTable="books"
issueTable="issued_books"


mypass="root"
mydatabase="mydb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()



def Viewissuebooks():
    subprocess.call(["python", "view_issued_books.py"])
 

def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("700x500")
        #background image
    image=Image.open("lib.jpg")

    # Resize the image using resize() method
    resize_image = image.resize((700, 500))
 
    img = ImageTk.PhotoImage(resize_image)

     
# create label and add resize image
    label6 = Label(image=img)
    label6.image = img
    label6.pack()

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %40s %30s %20s"%('BID','Title','Author','Status'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "--------------------------------------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25
    
    #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    getBooks = "select * from books order by bid asc ";
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s"%(i[0],i[1],i[2],i[3]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
        messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="QUIT", bg='#0048ff', fg="white", command=root.destroy)
    quitBtn.place(relx=0.5, rely=0.9, relwidth=0.18, relheight=0.08)

    #issue books 
    quitBtn = Button(root, text="Issue Books ", bg='#0048ff', fg="white",command=Viewissuebooks)
    quitBtn.place(relx=0.3, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

View()
