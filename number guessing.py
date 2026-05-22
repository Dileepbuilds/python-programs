import random
def guessing_game():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f" correct! You got it in {attempts} attempts! ")
            break

guessing_game()