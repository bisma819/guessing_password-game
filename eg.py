
import random

easy_words = ["apple", "car", "bus", "lion", "money"]
medium_words = ["python", "bottle", "money", "planet", "laptop"]
hard_words = ["umbrella", "diamond", "elephant", "mountain"]

print("Welcome to the password guessing game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break

    # Build hint
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]   # correct letter in correct place
        else:
            hint += "_"        # placeholder for wrong/missing letter

    print("Hint:", hint)

print("Game over.")
