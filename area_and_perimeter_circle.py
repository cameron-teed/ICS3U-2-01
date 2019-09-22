#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the area and perimeter of a circle with the
#   radius of 20mm

import math


def main():
    print("If a circle has a radius of 20mm:")
    print("")
    print("Area is {}cm^2".format(math.pi*20**2))
    print("Perimeter is {}cm".format(2*math.pi*20))


if __name__ == "__main__":
    main()
