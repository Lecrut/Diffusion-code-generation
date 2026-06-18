import calendar
from datetime import datetime
def validate_date(year: int, month: int, day: int) -> bool:
    if not (1 <= year <= 9999):
        return False
    if not (1 <= month <= 12):
        return False
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = days_in_month[month - 1]
    return day <= max_day
def generate_date_string(year: int, month: int, day: int) -> str:
    if not validate_date(year, month, day):
        raise ValueError(f"Invalid date provided: {year}-{month}-{day}")
    try:
        dt = datetime(year, month, day)
        return f"{dt.strftime('%B %d, %Y')}"
    except ValueError as e:
        raise
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    try:
        result_date_string = generate_date_string(sample_year, sample_month, sample_day)
        print(f"Valid Date String: {result_date_string}")
        test_invalid = (2023, 13, 5)
        if not validate_date(*test_invalid):
            try:
                generate_date_string(*test_invalid)
            except ValueError as ve:
                print(f"Caught expected error for {test_invalid}: {ve}")
    except Exception as e:
        print(f"Error occurred during generation or validation: {e}")