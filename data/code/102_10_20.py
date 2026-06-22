import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    day_code = calendar.weekday(dt.year, dt.month, dt.day)
    return day_code <= 4

if __name__ == '__main__':
    test_datetime = datetime(2023, 10, 23)
    print(is_weekday(test_datetime))