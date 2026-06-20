import datetime

def validate_years(year1: int, year2: int) -> None:
    if not (isinstance(year1, int) and isinstance(year2, int)):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years must be non-negative.")

def calculate_year_difference(year1: int, year2: int) -> int:
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        year1 = 2023
        year2 = 1998
        difference = calculate_year_difference(year1, year2)
        print(f"Year 1: {year1}")
        print(f"Year 2: {year2}")
        print(f"The absolute difference between the two years is: {difference}")
    except ValueError as e:
        print(e)