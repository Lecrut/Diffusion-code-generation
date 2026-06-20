import sys

def calculate_year_difference(year1, year2):
    try:
        return abs(int(year1) - int(year2))
    except ValueError:
        print("Error: Both inputs must be integers.")
        return None

if __name__ == '__main__':
    result = calculate_year_difference('2023', '2019')
    if result is not None:
        print(result)