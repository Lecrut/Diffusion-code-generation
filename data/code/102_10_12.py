import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    day_code = calendar.weekday(dt.year, dt.month, dt.day)
    return day_code in (0, 1, 2, 3, 4)

if __name__ == '__main__':
    test_date = datetime(2023, 10, 23)
    result = is_weekday(test_date)
    print(result)
    test_weekend = datetime(2023, 10, 21)
    print(is_weekday(test_weekend))