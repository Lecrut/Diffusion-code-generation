import sys

def calculate_year_difference(year1, year2):
    try:
        return abs(int(year1) - int(year2))
    except ValueError:
        return "Error: Both inputs must be integers."

if __name__ == '__main__':
    print(calculate_year_difference('2023', '2020'))