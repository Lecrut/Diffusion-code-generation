import calendar
from datetime import date

def is_weekday(d):
    if not isinstance(d, date):
        return False
    try:
        day_num = calendar.weekday(d.year, d.month, d.day)
        return day_num < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    test_date = date(2024, 5, 20)
    print(is_weekday(test_date))