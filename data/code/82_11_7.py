MIN_YEAR = 1582

def calculate_year_difference(year1: int, year2: int) -> int:
    if year1 < MIN_YEAR or year2 < MIN_YEAR:
        raise ValueError("Year values must be after the Gregorian calendar reform in 1582.")
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        difference = calculate_year_difference(2023, 1990)
        print(difference)
        difference = calculate_year_difference(2000, 2024)
        print(difference)
        difference = calculate_year_difference(1850, 1850)
        print(difference)
    except ValueError as e:
        print(e)