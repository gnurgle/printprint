import win32ui
import win32con

def printprint(message):
    # Convert tabs to spaces
    message.replace('\t', '  ')

    if len(message) < 28:
        printText(message)

    #Split at newlines
    splitmsg = message.splitlines()
    newmsg = ""
    for element in splitmsg:
        newmsg += element
        if len(element) < 28:
            for i in range (len(element),28):
                newmsg += " "

    printText(newmsg)

def printText(message):

    linenum = 0
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC()
    dc.StartDoc("")

    dc.StartPage()

    dc.SetMapMode(win32con.MM_TWIPS)

    #Crude text wrap
    for i in range(0,len(message), 28):
        dc.TextOut(10,linenum,message[i:i+28])
        linenum += -220

    dc.EndPage()
    dc.EndDoc()
