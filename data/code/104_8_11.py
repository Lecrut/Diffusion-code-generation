from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1, date2):
    delta = relativedelta(date1, date2)
    days_diff = abs(delta.days)
    if delta.days < 0:
        days_diff += 30
    return days_diff <= 7

if __name__ == '__main__':
    d1 = datetime(2023, 10, 1)
    d2 = datetime(2023, 10, 5)
    result = is_within_one_week(d1, d2)
    print(result)