def validate_years(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")

def calculate_year_difference(year1, year2):
    validate_years(year1, year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    result = calculate_year_difference(2023, 1985)
    print(result)