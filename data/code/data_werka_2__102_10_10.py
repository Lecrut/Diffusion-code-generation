import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Argument must be a datetime instance")
    return calendar.weekday(dt.year, dt.month, dt.day) in (0, 1, 2, 3, 4)

if __name__ == '__main__':
    dt_sample = datetime(2023, 10, 23)
    print(is_weekday(dt_sample))