import calendar
from datetime import date

def is_weekday(d: date) -> bool:
    try:
        weekday_num = calendar.weekday(d.year, d.month, d.day)
        return weekday_num < 5
    except AttributeError:
        return False

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)