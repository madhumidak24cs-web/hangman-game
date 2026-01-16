import random

# List of predefined words
words = ["apple", "tiger", "chair", "robot", "snake"]

# Randomly choose a word
secret_word = random.choice(words)
guessed = ["_"] * len(secret_word)
attempts = 6
used_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word letter by letter!")
print("Word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter a single letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
    print()

# Result
if "_" not in guessed:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("❌ Out of attempts! The word was:", secret_word)
