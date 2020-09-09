from tkinter import *
import random


root = Tk()
root.title("Team Creator - Zayd")
#root.iconbitmap("icon.ico")
root.geometry("400x400")

title = Label(root, text="Separate each name with a comma").pack()

input = Entry(root)
input.pack()


def myClick():
    inputToString = str(input.get())
    stringToList = inputToString.split(", ")
    random.shuffle(stringToList)
    Team1 = stringToList
    lenTeam1 = len(Team1)
    print(Team1)
    middle_index = lenTeam1//2
    Team1half = Team1[:middle_index]
    Team2half = Team1[middle_index:]
    aTeam1Str = str(Team1half)
    aTeam2Str = str(Team2half)
    Team1Str = aTeam1Str.replace("'", "")
    Team2Str = aTeam2Str.replace("'", "")
    # print(Team1Str, Team2Str)
    T1results = Label(root, text="Team 1 : " + Team1Str, fg="blue").pack()
    T2results = Label(root, text="Team 2 : " + Team2Str, fg="blue").pack()

myButton = Button(root, text="Click Me", command = myClick)
myButton.pack()

root.mainloop()
