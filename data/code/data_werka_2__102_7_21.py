import calendar
from datetime import date

def validate_date_object(candidate):
    if not hasattr(candidate, 'year') or not hasattr(candidate, 'month') or not hasattr(candidate, 'day'):
        raise ValueError("Input must be a date-like object with year, month, and day attributes")
    return True

def determine_weekday_status(target_date):
    validate_date_object(target_date)
    try:
        day_index = calendar.weekday(target_date.year, target_date.month, target_date.day)
        return day_index < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    sample = date(2023, 10, 23)
    result = determine_weekday_status(sample)
    print(result)