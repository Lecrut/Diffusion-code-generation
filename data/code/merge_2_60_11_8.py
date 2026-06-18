import sys
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def validate_input(value):
    if not isinstance(value, int):
        raise TypeError(f"Expected an integer for 'year', got {type(value).__name__}")
    if value < -9000 or value > 30000:
        raise ValueError(f"Year must be between -9000 and 30000, got {value}")
if __name__ == '__main__':
    test_cases = [2000, 1900, 2024, 2023, -8765]
    print("Leap Year Validation Results:")
    try:
        for year in test_cases:
            validate_input(year)
            if is_leap_year(year):
                status = "LEAP YEAR"
            else:
                status = "NOT A LEAP YEAR"
            print(f"{year}: {status}")
    except (TypeError, ValueError) as e:
        print(f"Error processing input: {e}")