#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program to calculates the total cost for a given diameter pizza.

import constants


def main():
    # This is the funciton to calculate the total cost of pizza.

    # Input
    diameter = int(input("Enter the diameter of the pizza (inch)"))

    # Process
    without_hst = (constants.rent + constants.labor +
                   constants.materials * diameter)
    final = without_hst * constants.hst

    # Output
    print("")
    print("The prize is ${}".format(final))


if __name__ == "__main__":
    main()
