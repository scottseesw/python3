#This module has 2 functions: 1) to calculate area ans 2) circumference of a circle
def calculate_square_footage():
    try:
        length = float(input("Enter the length of the house (in feet): "))
        width = float(input("Enter the width of the house (in feet): "))

        square_footage = length * width
        print(f"The square footage of the house is: {square_footage} square feet.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for length and width.")


if __name__ == "__main__":
    calculate_square_footage()

# This is a function getting user input to calculate the 
#circumference of a circle

import math
30
def calculate_circumference():
    try:
        radius = float(input("Enter the radius of the circle (in units): "))
        circumference = 2 * math.pi * radius
        print(f"The circumference of the circle is: {circumference:.2f} units.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the radius.")

if __name__ == "__main__":
    calculate_circumference()