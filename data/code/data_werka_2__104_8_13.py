from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    abs_days = abs(delta.days)
    if abs_days > 7:
        return False
    if abs_days == 7:
        return abs(delta.hours) + abs(delta.minutes) + abs(delta.seconds) == 0
    return True

if __name__ == '__main__':
    d1 = datetime(2023, 10, 1, 12, 0, 0)
    d2 = datetime(2023, 10, 8, 12, 0, 0)
    result = is_within_one_week(d1, d2)
    print(result)