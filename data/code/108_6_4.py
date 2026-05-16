import sys
def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False, "Invalid date components provided."
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False, "Invalid day for the given month (must be <= 30)."
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap and day > 29:
            return False, "Invalid day for February in a leap year (must be <= 29)."
        if not is_leap and day > 28:
            return False, "Invalid day for February in a common year (must be <= 28)."
    if month == 10 or month == 12:
        if day > 31:
            return False, "Invalid day for months with 31 days (must be <= 31)."
    return True, day
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 2
    sample_day = 30
    try:
        is_valid, result = validate_date(sample_year, sample_month, sample_day)
        if is_valid:
            print(result)
        else:
            print(f"Error: {result}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")