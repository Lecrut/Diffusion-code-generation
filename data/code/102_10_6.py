import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("dt must be a datetime instance")
    day_code = calendar.weekday(dt.year, dt.month, dt.day)
    return 0 <= day_code <= 4

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)