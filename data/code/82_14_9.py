def validate_year(year: int) -> None:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if year < 0:
        raise ValueError("Year cannot be negative")

def absolute_year_difference(year1: int, year2: int) -> int:
    validate_year(year1)
    validate_year(year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    print(absolute_year_difference(2060, 2005))