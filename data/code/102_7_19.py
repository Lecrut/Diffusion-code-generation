import calendar
from datetime import date

def validate_and_check_weekday(target_date):
    if not isinstance(target_date, date):
        raise ValueError("Input must be a date object")
    try:
        day_of_week = calendar.weekday(target_date.year, target_date.month, target_date.day)
        return day_of_week < 5
    except (AttributeError, OverflowError) as e:
        raise ValueError("Date components are invalid or out of range") from e

if __name__ == '__main__':
    today = date(2023, 10, 23)
    is_week = validate_and_check_weekday(today)
    print(is_week)