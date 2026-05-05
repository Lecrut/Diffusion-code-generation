import sys
def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    difference = calculate_difference(year1, year2)
    print(difference)