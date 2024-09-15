import random

def guess_the_number():
  """A simple game where the user tries to guess a random number."""

  random_number = random.randint(1, 100)
  attempts = 0

  while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess == random_number:
      print(f"Congratulations! You guessed the number in {attempts} attempts.")
      break
    elif guess < random_number:
      print("Too low. Try again.")
    else:
      print("Too high. Try again.")

if __name__ == "__main__":
  guess_the_number()