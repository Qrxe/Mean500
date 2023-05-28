import random

while True:
    randomness = 0
    count = int(input("How many numbers would you like to add to the mean?: "))

    for i in range(0, count, 1):
        randomness += random.randint(1, 1000)

    print(randomness / count)
    again = input("\nWould you like to try again? (y/n): ").lower()
    print("\n")
    if again == "n" or not "y":
        break