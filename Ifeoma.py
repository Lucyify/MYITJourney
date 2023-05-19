import PySimpleGUI as psg
from  PIL import Image
def resize(img, dim:tuple):
    img = Image.open(img)
    sv = img.resize(dim)
    sv.save("./new.png")
layout=[
    [
        psg.Input(key="filepath", expand_x=True),
        psg.FileBrowse("select Image", key="-browse-"),
    ],
    [psg.Image(key="img", background_color="white", expand_x=True, expand_y=True)],
    [psg.Text("width", expand_x=True,),psg.Input(key="-width-", expand_x=True), psg.Text("height", expand_x=True), psg.Input(key="-height-", expand_x=True),psg.Button("resize",expand_x=True)],
]
win = psg.Window("ify Image Resizer", layout, resizable=True, size=(900,600))
while True:
    evt, vals = win.Read(0)
    print(evt, vals)
    if vals["-browse-"] != "":
        win["filepath"].Update(value=vals["-browse-"])
        win["img"].Update(source=vals["-browse-"])
    if evt == "resize":
        resize(vals["filepath"], (int(vals["-width-"]), int(vals["-height-"])))     