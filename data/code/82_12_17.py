def validate_years(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Year values must be non-negative.")

def calculate_year_difference(year1, year2):
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    start_year = 2023
    end_year = 1985
    diff = calculate_year_difference(start_year, end_year)
    print(diff)