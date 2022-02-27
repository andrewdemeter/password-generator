import string
import random

# Prompt the user to enter their desired password type
type = input("What type of password would you like to generate?\n"
               "• Characters (C),\n"
               "• Characters + Digits (CD),\n"
               "• or Characters + Digits + Symbols (CDS)\n")

# If the user enters something other than "C", "CD", or "CDS"...
while type.upper() != "C" and type.upper() != "CD" and type.upper() != "CDS":
    type = input("You must enter C, CD, or CDS...\n")

# Prompt the user to enter their desired password length
length = input("Enter the desired length of your password (1-64 characters)...\n")

# If the user enters something other than a digit between 1-64...
while length.isdigit() is False or int(length) not in range(1, 65, 1):
    length = input("You must enter a number between 1-64...\n")

# If the user entered the Characters password type...
if type.upper() == "C":
    # Create a variable with the entire alphabet (capital and lowercase)
    values = string.ascii_letters

# If the user entered the Characters + Digits password type...
if type.upper() == "CD":
    # Create a variable with the entire alphabet (capital and lowercase) and digits 0-9
    values = string.ascii_letters + string.digits

# If the user entered the Characters + Digits + Symbols password type...
if type.upper() == "CDS":
    # Create a variable with the entire alphabet (capital and lowercase), digits 0-9,
    # and symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    values = string.ascii_letters + string.digits + string.punctuation

# Create a variable that will count each iteration of the while loop below
index = 0

# Create a variable that will store the password
password = ""

# Run this loop as many times as the user's desired password length
while index < int(length):
    # Choose a random value from the list of possible values, then add it to the password variable
    password = password + random.choice(values)
    # Increment the index variable by 1
    index += 1

# Print the randomly generated password
print("Your password is: " + password)