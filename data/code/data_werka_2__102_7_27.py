import calendar
from datetime import date

def get_weekday_status(target_date):
    if not isinstance(target_date, date):
        raise ValueError("Input must be a date instance")
    try:
        day_code = calendar.weekday(target_date.year, target_date.month, target_date.day)
        return day_code < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    test_date = date(2024, 10, 28)
    status = get_weekday_status(test_date)
    print(status)