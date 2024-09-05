import random as rd
C_number=rd.randrange(1,101)
U_number=int(input("Enter your Guess Number (between 1 and 100):"))
if U_number>C_number:
    print("Computer Number:", C_number)
    print("Your Guess Number is too high")
elif U_number<C_number:
    print("Computer Number:", C_number)
    print("Your Guess Number is too low")
else:
    print("Computer Number:", C_number)
    print("Congratulation! You won your guess number is equal to computer number")