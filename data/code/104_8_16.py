from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(first_date: datetime, second_date: datetime) -> bool:
    delta = relativedelta(first_date, second_date)
    if delta.years != 0 or delta.months != 0:
        return False
    if delta.days < 0:
        return delta.days >= -7
    return delta.days <= 7

if __name__ == '__main__':
    d1 = datetime(2023, 10, 1, 12, 0, 0)
    d2 = datetime(2023, 10, 8, 12, 0, 0)
    print(is_within_one_week(d1, d2))