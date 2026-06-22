import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    day_of_week = calendar.weekday(dt.year, dt.month, dt.day)
    return day_of_week < 5

if __name__ == '__main__':
    test_date = datetime(2023, 10, 23)
    print(is_weekday(test_date))
    test_weekend = datetime(2023, 10, 21)
    print(is_weekday(test_weekend))