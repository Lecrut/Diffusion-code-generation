import sys

def calculate_year_difference(year1, year2):
    if not (isinstance(year1, int) and isinstance(year2, int)):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        year1 = 2024
        year2 = 1999
        difference = calculate_year_difference(year1, year2)
        print(difference)
    except ValueError as e:
        print(e)