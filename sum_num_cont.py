#!/usr/bin/env python3

# created by: Paterry Baptichon
# created on: 2022-05-01
# this program lets user decide amount of number to be inputed and what numbers
# will be inputed and calculates the sum of the numbers entered

def main():
    # This is the function to run while loop.
    
    loop_counter = 0
    final = 0
    # Input of the user
    user_input_number = input("How many numbers are you going to add:")
    print("")

    # proccess of the program
    # converting str to int
    try:
        user_input_number = int(user_input_number)
        if user_input_number > 0:
            while loop_counter < user_input_number:
                inputnumber = input("Enter  integer to add:")
                inputnumber = int(inputnumber)
                if inputnumber < 0:
                    final = final + 0
                   # add it to the current sum BUT if it is negative do not add
                    loop_counter = loop_counter + 1
                    continue
                else:
                    while_number = inputnumber
                    final = while_number + final
                    loop_counter = loop_counter + 1
                continue
            # Display the numbers added and the final sum to the user.
            print("The total is {}".format(final))
        elif user_input_number < 0:
            print("Sorry, you did not enter a positive integer!")
    except Exception:
        print("You are not type in an integer!")


if __name__ == "__main__":
    main()