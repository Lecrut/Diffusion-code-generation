from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = abs((date1 - date2).days)
    return delta <= 7

if __name__ == '__main__':
    d1 = datetime(2023, 10, 1)
    d2 = datetime(2023, 10, 5)
    result = is_within_one_week(d1, d2)
    print(result)