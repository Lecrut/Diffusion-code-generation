from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    days_diff = delta.days
    if days_diff < 0:
        days_diff = -days_diff
    return days_diff <= 7

if __name__ == '__main__':
    d1 = datetime(2023, 10, 10)
    d2 = datetime(2023, 10, 15)
    result = is_within_one_week(d1, d2)
    print(result)