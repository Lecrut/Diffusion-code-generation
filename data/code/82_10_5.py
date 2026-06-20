def validate_year(year):
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a non-negative integer.")

def calculate_year_difference(year1, year2):
    validate_year(year1)
    validate_year(year2)
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        result = calculate_year_difference(2023, 1985)
        print(result)
    except ValueError as e:
        print(e)