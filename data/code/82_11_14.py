def validate_year(year: int) -> None:
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a non-negative integer")

def calculate_year_difference(year1: int, year2: int) -> int:
    validate_year(year1)
    validate_year(year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    difference = calculate_year_difference(2023, 1990)
    print(difference)