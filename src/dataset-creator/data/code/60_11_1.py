import sys
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def validate_input(value):
    if not isinstance(value, int):
        raise TypeError(f"Input must be an integer, got {type(value).__name__}")
    if value < 1 or value > 9999:
        raise ValueError("Year must be between 1 and 9999")
if __name__ == '__main__':
    test_cases = [2000, 2024, 1900, -5, "invalid", None]
    try:
        for year in test_cases:
            validate_input(year)
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
    except (TypeError, ValueError) as e:
        print(f"Error processing input {e}:")