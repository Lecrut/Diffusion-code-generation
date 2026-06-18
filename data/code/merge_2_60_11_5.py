import sys
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def validate_input(value):
    if not isinstance(value, int):
        raise TypeError(f"Input must be an integer, got {type(value).__name__}")
    min_year = 1
    max_year = 2500
    if value < min_year or value > max_year:
        raise ValueError(f"Year must be between {min_year} and {max_year}, got {value}")
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, -5]
    try:
        for year in test_years:
            validate_input(year)
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
    except (TypeError, ValueError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)