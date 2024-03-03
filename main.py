import random

def guess_the_number():
    comp_guess = random.randint(1, 100)
    print("Guess the number. It is between 1 and 100")
    user_guess = 0
    while user_guess != comp_guess:
        user_guess = int(input("Type in your guess: "))
        if user_guess > comp_guess:
            print("Too high")
        elif user_guess < comp_guess:
            print("Too low")
        else:
            print("You guessed correct!")




if __name__ == '__main__':
    guess_the_number()

