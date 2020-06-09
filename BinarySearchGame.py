def calculate_midpoint(lower_bound: int, higher_bound: int):
    return lower_bound + (higher_bound - lower_bound) // 2


current_low = 1
current_high = 1000

print("Please think of a number between {} and {}.".format(current_low, current_high))
input("press ENTER to start")
print("*" * 40)

guesses = 1

while current_low != current_high:

    current_guess = calculate_midpoint(current_low, current_high)

    user_input = input(
        "\nMy guess is {}.\n" 
        "Should I guess higher or lower? \n\n"
        "Enter h for higher or l for lower. "
        "If my guess was correct enter c. "
        .format(current_guess)).casefold()

    if user_input == "h":
        current_low = current_guess + 1
    elif user_input == "l":
        current_high = current_guess - 1
    elif user_input == "c":
        print("\nYou thought of a number {}".format(current_guess))
        print("I got it in {} guess(es)!".format(guesses))
        break
    else:
        print("Please enter h, l or c as advised.")
    guesses += 1
else:
    print("\nYou thought of a number {}".format(current_low))
    print("I got it in {} guess(es)!".format(guesses))
