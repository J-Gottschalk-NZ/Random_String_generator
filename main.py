import string
import random

# Function to check string length is an integer that is > 0
def intcheck(question):
  
  error = "Please enter an integer that is more than 0 \n"
  
  valid = False
  while not valid:
    
    try:
      response = int(input(question))

      if response < 1:
        print(error)
      else:
        return response

    except ValueError:
      print(error)

# Create string including letters, digits and symbols
random_characters = string.ascii_letters + string.digits + string.punctuation

how_many = intcheck("How many characters? ")

random_string = ""
for item in range(0,how_many):

  random_char = random.choice(random_characters)
  random_string += random_char

print(random_string)