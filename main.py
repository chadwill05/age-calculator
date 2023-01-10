import tkinter as tk
from datetime import datetime


class AgeCalculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Age Calculator")

        # Create a label for the birthday input
        self.bday_label = tk.Label(self, text="Enter your birthday (mm/dd/yyyy):")
        self.bday_label.pack()

        # Create a text entry box for the birthday input
        self.bday_entry = tk.Entry(self)
        self.bday_entry.pack()

        # Create a button to calculate age
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_age)
        self.calculate_button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate_age(self):
        # Get the birthday from the text entry box
        bday_str = self.bday_entry.get()
        # Parse the birthday string into a datetime object
        bday = datetime.strptime(bday_str, "%m/%d/%Y")
        # Calculate the age in years
        today = datetime.now()
        age = today.year - bday.year
        if (today.month, today.day) < (bday.month, bday.day):
            age -= 1
        # Update the result label with the age
        self.result_label["text"] = f"You are {age} years old."


app = AgeCalculator()
app.mainloop()
