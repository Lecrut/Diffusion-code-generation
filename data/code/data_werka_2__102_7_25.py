import calendar
from datetime import date

def is_weekday(d):
    if not isinstance(d, date):
        raise ValueError("Invalid input type")
    try:
        return calendar.weekday(d.year, d.month, d.day) < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    result = is_weekday(test_date)
    print(result)