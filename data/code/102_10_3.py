import calendar
from datetime import datetime

WEEKDAY_STATUS = {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: False,
    6: False,
}

def is_weekday(dt: datetime) -> bool:
    day_index = calendar.weekday(dt.year, dt.month, dt.day)
    return WEEKDAY_STATUS[day_index]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)