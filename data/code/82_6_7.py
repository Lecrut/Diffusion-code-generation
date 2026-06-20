def validate_years(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")

def year_difference(year1, year2):
    validate_years(year1, year2)
    return year1 - year2

if __name__ == '__main__':
    print(year_difference(2024, 2020))
    print(year_difference(1990, 2000))
    print(year_difference(2025, 2025))
    print(year_difference(1800, 1900))