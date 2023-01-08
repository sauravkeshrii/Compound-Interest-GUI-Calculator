from tkinter import*

# defining the reset function :
def reset() :
    principalField.delete(0, END)
    rateField.delete(0, END)
    numberField.delete(0, END)
    timeField.delete(0, END)
    resultField.delete(0, END)
    
    principalField.focus_set()
    
# defining the function to calculate the compound interest

def compound_interest():
    principal = float(principalField.get())
    rate_of_interest = float(rateField.get())
    number = float(numberField.get())
    time = float(timeField.get())
        
    amount = principal * pow((1 + (rate_of_interest/(100*number))),number*time)
        
    ci = amount - principal
        
    resultField.insert(10, ci)
        
# Creating the main window for the application :

if __name__=="__main__":
    
    guiWindow = Tk()
    guiWindow.title("Compound Interest Calculator")
    guiWindow.geometry('500x500')
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#f0c33c")
    
# Adding widgets to the main window ::

# heading 
guiLabel = Label(
    guiWindow,
    text="CALCULATE THE COMPOUND INTEREST",
    font = ("Arial", 20),
    fg = "#211600",
    bg = "#f0c33c"
    )

guiLabel.place(
    x = 60,
    y= 10
    )

# Principal Amount Label
labelOne = Label(
    guiWindow,
    text= "Principal Amount(Rs.):",
    bg= "#f0c33c",
    fg="#4a3200"
)

labelTwo = Label(
    guiWindow,
    text= "Rate of Interest(%):",
    bg= "#f0c33c",
    fg="#4a3200"
)

labelThree = Label(
    guiWindow,
    text= "No. of Times(n): ",
    bg= "#f0c33c",
    fg="#4a3200"
)

labelFour = Label(
    guiWindow,
    text= "Time Period(Years):",
    bg= "#f0c33c",
    fg="#4a3200"
)

labelFive = Label(
    guiWindow,
    text= "Compound Interest(C.I.)",
    bg= "#f0c33c",
    fg="#4a3200"
)

# Place() method to place the above labels on the window :

labelOne.place(x=72, y=120)
labelTwo.place(x=72, y=160)
labelThree.place(x=72, y=200)
labelFour.place(x=72, y=240)
labelFive.place(x=72, y=340)

# Use Entry() to add some entry fields to main window

principalField = Entry(
    guiWindow,
    bg= "#fcf9e8",
    fg="#211600"
)

rateField = Entry(
    guiWindow,
    bg= "#fcf9e8",
    fg="#211600"
)

numberField = Entry(
    guiWindow,
    bg= "#fcf9e8",
    fg="#211600"
)

timeField = Entry(
    guiWindow,
    bg= "#fcf9e8",
    fg="#211600"
)

resultField = Entry(
    guiWindow,
    bg= "#fcf9e8",
    fg="#211600"
)

# Using Place() method to place the above fields on the window:

principalField.place(x=250, y=120)
rateField.place(x=250, y=160)
numberField.place(x=250, y=200)
timeField.place(x=250, y=240)
resultField.place(x=250, y=340)

# creating a Result button :
resultButton = Button(
    guiWindow,
    text="CALCULATE",
    bg="#134e96",
    fg="#fcf9e8",
    command= compound_interest
)

# Creating the Reset button :
resetButton = Button(
    guiWindow,
    text="RESET",
    bg="#d63638",
    fg="#fcf0f1",
    command= reset
)

# Place() the buttons on window
resultButton.place(x=280, y=280)
resetButton.place(x=300, y=380)

guiWindow.mainloop()