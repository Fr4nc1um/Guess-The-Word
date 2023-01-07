import random

# The puzzle is a list of strings
puzzle = [
    "gigabit",
    "ethernet",
    "protocol",
    "packet",
    "router",
    "firewall",
]

# Pick a random word from the puzzle
word = random.choice(puzzle)

# Convert the word to a list of characters
word_chars = list(word)

# Shuffle the list of characters
random.shuffle(word_chars)

# Join the list of characters back into a single string
scrambled_word = "".join(word_chars)

# Print the scrambled word
print(scrambled_word)

# Ask the user to guess the original word
guess = input("What is the original word? ")

# Check if the guess is correct
if guess == word:
    print("Correct! Well done.")
else:
    print("Incorrect. The correct answer is", word)
