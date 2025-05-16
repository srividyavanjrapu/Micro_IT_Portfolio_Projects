import random

number = random.randint(1,100)
guess = 0
attempts = 0
max_attempts = 3


print("guess the number between 1 to 100")
print(f"you have {max_attempts} attempts")

while guess != number and attempts < max_attempts:
    guess = int(input("enetr guess:"))
    attempts += 1

    if guess < number:
        print("guess higher!")
    elif guess > number:
        print("guess lower1")
    else:
        print(f"you won in {attempts} attempts")

if guess != number:
    print(f"sorry,you ran out of attempts.the number was {number} ")