#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program rounds numbers


def round_number(user_enter, user_decimal):
    # This function rounds numbers
    number_round = user_enter[0] * 10 ** user_decimal
    number_round = int(number_round + 0.5)
    number_round = number_round / (10 ** user_decimal)

    user_enter[0] = number_round


def main():
    # this is the main function
    user_enter = []

    try:
        user_number = input("Enter the number you want to round : ")
        user_number = float(user_number)
        user_decimal = input("Enter how many numbers you want to round : ")
        user_decimal = int(user_decimal)

        user_enter.append(user_number)

        round_number(user_enter, user_decimal)

        print("The rounded number is {0}".format(user_enter[0]))

    except (Exception):
        print("\nInvalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
