import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Input the number of letters in the password
nr_letter = int(input("How many letters would you like in your password?\n"))

# Input the number of symbols in the password
nr_symbol = int(input("How many symbols would you like?\n"))

# Input the number of numbers in the password
nr_number = int(input("How many numbers would you like?\n"))

# password is an empty list
password = []

for i in range(0, nr_letter):
    random_letters = random.randint(0, len(letters) - 1)
    password.append(letters[random_letters])
    
for i in range(0, nr_symbol):
    random_symbols = random.randint(0, len(symbols) - 1)
    password.append(symbols[random_symbols])
    
for i in range(0, nr_number):
    random_numbers = random.randint(0, len(numbers) - 1)
    password.append(numbers[random_numbers])
    
# This gives password as a string rather than a list. This also gives is the password as a string consisting nr_letter number of letters, then nr_symbol number of symbols and finally nr_number number of symbols. No shuffling.
print(f"Your password is: {''.join(password)}")

# This is used to shuffle the above generated password and give a different combination of the password.
random.shuffle(password)

print(f"Your password is: {''.join(password)}")
