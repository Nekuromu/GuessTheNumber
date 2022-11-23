from random import randint

attempts = 0
difficulty = ""
guess = 0
goal_num = randint(1, 100)

print(f"TEST: {goal_num}")


def make_guess(input_int):
    if int(input_int) < goal_num:
        return -1
    elif int(input_int) == goal_num:
        return 0
    else:
        return 1


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
while not difficulty == "easy" and not difficulty == "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid answer. Try Again.")

while attempts >= 1:

    print(f"You have {attempts} remaining to guess the number.")

    guess = input("Make a guess: ")
    compare_var = make_guess(guess)

    if compare_var == -1:
        print("Too low.")
        attempts -= 1
        compare_var = -2
    elif compare_var == 1:
        print("Too high")
        attempts -= 1
        compare_var = -2
    elif compare_var == 0:
        break
    else:
        print(f"ERROR, UNEXPECTED OUTCOME: {compare_var}")

if attempts <= 0:
    print("You've run out of guesses, you lose.")
else:
    print(f"The answer was {goal_num}, you win!")