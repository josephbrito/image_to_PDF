import PySimpleGUI as sg
from PIL import Image


layout = [
         [sg.Text("Image to PDF")],
         [sg.Text("Path image", size=(10, 1)), sg.FileBrowse("FileBrowse")],
         [sg.Button("Save PDF")]
         ]


window =  sg.Window("Made by José de Brito", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Save PDF":
        img1 = Image.open(values["FileBrowse"])
        img_s = img1.convert("RGB")
        path = values["FileBrowse"]
        print(path)
        img_s.save(path + ".pdf")



window.close()

