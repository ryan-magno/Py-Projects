import random


def guess_number(guess):
    num = random.randint(1, 11)
    if guess < num:
        print("Too low")
    if guess > num:
        print("Too high")
    if guess == num:
        print("You guessed it!")
    print("Try again?")
    print("The number was: ", num)
    return

if __name__ == "__main__":
    guess_number(5)
