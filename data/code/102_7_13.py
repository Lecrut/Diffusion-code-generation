import calendar
from datetime import date

WORKDAY_THRESHOLD = 5

def is_weekday(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be a date instance")
    try:
        day_index = calendar.weekday(date_obj.year, date_obj.month, date_obj.day)
        return day_index < WORKDAY_THRESHOLD
    except AttributeError:
        return False

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    result = is_weekday(test_date)
    print(result)