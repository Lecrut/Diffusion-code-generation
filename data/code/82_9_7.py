import sys

def calculate_year_difference(year1, year2):
    try:
        year1 = int(year1)
        year2 = int(year2)
        return abs(year1 - year2)
    except ValueError:
        raise ValueError("Both inputs must be integers")

if __name__ == '__main__':
    year1 = 2024
    year2 = 1999
    difference = calculate_year_difference(year1, year2)
    print(difference)