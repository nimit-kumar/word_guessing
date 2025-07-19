import random

def function(choice):
    guess_count = 0
    word_length = len(choice)
    while True:
        user_guess = input("Enter word to guess:\n").lower()
        guess_count += 1

        if user_guess == choice:
            print(f"\n🎉 Congratulations! You won the game.")
            print(f"You guessed the word in {guess_count} attempts.")
            break
        else:
            # Generate hint: correct letters in correct positions
            display = ""
            for i in range(word_length):
                if i < len(user_guess) and user_guess[i] == choice[i]:
                    display += user_guess[i] + " "
                else:
                    display += "_ "
            print(f"❌ Wrong guess! Here's your hint: {display.strip()}\n")

easy_words = ['car', 'dog', 'bat', 'map', 'sun']
medium_words = ['apple', 'train', 'tiger', 'money', 'india']
hard_words = ['diamond', 'journey', 'monitor', 'laptop', 'mission']

print("🔠 Welcome to the Word Guessing Game!\n")
print("📝 Rules:")
print("1️⃣ Easy Level: 3-letter words")
print("2️⃣ Medium Level: 5-letter words")
print("3️⃣ Hard Level: 7-letter words")
print("💡 Hint: After each guess, correct letters in the correct position will be revealed.\n")

while True:
    try:
        level_choose = int(input("Select level:\n1 - Easy\n2 - Medium\n3 - Hard\nYour choice: "))
        if level_choose in [1, 2, 3]:
            if level_choose == 1:
                print("🟢 You chose Easy Level.\n")
                choice = random.choice(easy_words)
            elif level_choose == 2:
                print("🟡 You chose Medium Level.\n")
                choice = random.choice(medium_words)
            else:
                print("🔴 You chose Hard Level.\n")
                choice = random.choice(hard_words)
            function(choice)  # Don't use print(function(...)) as the function prints internally
            break
        else:
            print("❗ Invalid input! Enter 1, 2, or 3.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")
