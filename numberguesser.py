import random as r
num = r.randint(1,100)
guess = input("Guess my number (1-100):")
while int(guess) != num:
	print("lower" if int(guess)>num else "higher");
	guess = input("Next guess:")
print("you guessed correctly!")
