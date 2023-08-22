import qrcode
from tkinter import *
from tkinter import ttk

# website_link = input("Enter Link: ")
# qr = qrcode.QRCode(version=1, box_size= 5, border=5)

# qr.add_data(website_link)
# qr.make()

# fColor = input("Enter fill colour: ")
# bColor = input("Enter back colour: ")
# img = qr.make_image(fill_color = fColor, back_color = bColor)

# fName = input("Enter file name: ")
# img.save(fName + ".png")

def qr_generate(*args):
    try:
        site = str(link.get())
        qr = qrcode.QRCode(version=1, box_size= 5, border=5)

        qr.add_data(site)
        qr.make()
        fc = str(fColor.get())
        bc = str(bColor.get())
        img = qr.make_image(fill_color = fc, back_color = bc)

        file = str(fName.get())
        img.save(file + ".png")
    except ValueError:
        pass


root = Tk()
root.title("QRcode Generator")

mainframe = ttk.Frame(root, padding="15 12 15 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)

#link var
link = StringVar()
link_entry = ttk.Entry(mainframe, width=25, textvariable=link)
link_entry.grid(column=2, row=1, sticky=(W, E))
fName = StringVar()
fName_entry = ttk.Entry(mainframe, width = 25, textvariable=fName)
fName_entry.grid(column=2, row=2, sticky=(W, E))

#fcolor var
fColor = StringVar()
fColor_entry = ttk.Entry(mainframe, width=25,textvariable=fColor)
fColor_entry.grid(column=2, row=3, sticky=(W, E))

#bcolor var
bColor = StringVar()
bColor_entry = ttk.Entry(mainframe, width = 25, textvariable=bColor)
bColor_entry.grid(column=2, row=4, sticky=(W, E))

#button that will generate qrcode
ttk.Button(mainframe, text="Generate!", command=qr_generate).grid(column=2, row=5, sticky=E)

#labels aka plain texts on screen
ttk.Label(mainframe, text="Link :").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="File Name :").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Fill Colour :").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Background Colour :").grid(column=1, row=4, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

link_entry.focus()
root.bind("<Return>", qr_generate)

root.mainloop()
