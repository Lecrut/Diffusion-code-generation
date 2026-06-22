import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    return calendar.weekday(dt.year, dt.month, dt.day) < 5

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)