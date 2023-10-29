import random
# Letters, numbers and symbols to choose from stored in lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#initializing a while so that if the input is invalid the whole process goes back to the start
whileLoopControl=False

while whileLoopControl==False:
    # Initializing an empty password as string 
    password=""

    # Prompt the user for input followed by checks for the validity of the input
    print("\nWelcome to the PyPassword Generator!")
    # Choose the number of letters you want your password to have
    nrLetters= int(input("How many letters would you like in your password?\n")) 
    if nrLetters>len(letters):
        print("There are not that many letters in out list.")
        continue
    # Choose the number of symbols you want your password to have
    nrSymbols = int(input(f"How many symbols would you like?\n"))

    if nrSymbols>len(symbols):
        print("There are not that many letters in out list.")
        continue

    # Choose the number of numbers you want your password to have
    nrNumbers = int(input(f"How many numbers would you like?\n"))
    if nrNumbers>len(numbers):
        print("There are not that many letters in out list.")
        continue

    # Iterate through a spesific list and randomly pick the number of elements that were promted by the user
    # Iterations take place for letters, symbols and numbers separately
    for a in range(0,nrLetters):
        random_char=random.choice(letters)
        password+=random_char

    for b in range(0,nrNumbers):
        random_symb=random.choice(symbols)
        password+=random_symb

    for c in range(0,nrNumbers):
        random_numb=random.choice(numbers)
        password+=random_numb

    # Transform your password into a list for easy shuffle
    # If the shuffle does not take place, the password would keep the order in which the elements were added, so first the letters, then the symbols, and lastly the numbers.
    passwordList=[]

    # Adding each character in the password to a list
    for i in password:
        passwordList.append(i)
    # Shuffle the list
    random.shuffle(passwordList)
    # Making the list into a string again
    password="".join(passwordList)

    print("Your password is: "+password+". Make sure you keep it safe!")
    break

  


    
