import sys
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 100 != 0 and year % 4 == 0))
def validate_year(year_input):
    try:
        if isinstance(year_input, (int, float)):
            if not isinstance(year_input, int):
                year = int(float(year_input))
            else:
                year = int(year_input)
            if -1_000_000_000 <= year <= 1_000_000_000:
                return True
        raise TypeError("Input must be an integer or a numeric string.")
    except (ValueError, OverflowError):
        raise ValueError(f"Invalid input for year. Expected valid calendar year.")
if __name__ == '__main__':
    samples = [2000, 1900, 2024, -8765]
    print("Testing Leap Year Logic:")
    for year in samples:
        try:
            is_leap = validate_year(year) and is_leap_year(int(year)) if isinstance(year, str) else (validate_year(year), False)
            valid_input = True
            year_int = int(year)
        except Exception as e:
            print(f"Error processing {year}: {e}")
            continue
    test_cases = [2000, 1900, 2024]
    for year_val in test_cases:
        try:
            if isinstance(year_val, str):
                val_int = int(float(year_val))
            else:
                val_int = int(year_val)
            result = is_leap_year(val_int)
            print(f"Year {val_int}: {'Leap Year' if result else 'Not a Leap Year'}")
        except ValueError as ve:
            print(f"Invalid input for year {year_val}: {ve}")