def validate_years(year1: int, year2: int) -> bool:
    if not (isinstance(year1, int) and isinstance(year2, int)):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")
    return True

def calculate_year_difference(year1: int, year2: int) -> int:
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    print(calculate_year_difference(2023, 1990))
    print(calculate_year_difference(2000, 2024))
    print(calculate_year_difference(1850, 1850))