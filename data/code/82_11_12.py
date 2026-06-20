def calculate_year_difference(year1: int, year2: int) -> int:
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        difference = calculate_year_difference(2023, 1990)
        print(difference)
    except ValueError as e:
        print(e)