import sys
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def validate_input(value):
    if not isinstance(value, int):
        raise TypeError(f"Input must be an integer, got {type(value).__name__}")
    if value < 1 or value > 9999:
        raise ValueError("Year must be between 1 and 9999.")
if __name__ == '__main__':
    test_years = [2000, 2004, 2100, 2023]
    try:
        for year in test_years:
            validate_input(year)
            result = is_leap_year(year)
            print(f"Year {year} is a leap year: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)