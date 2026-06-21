from datetime import datetime
from dateutil.relativedelta import relativedelta

DATE_UNITS = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365
}

def is_within_one_week(first: datetime, second: datetime) -> bool:
    delta = relativedelta(first, second)
    total_days = delta.days
    if delta.hours > 0 or delta.minutes > 0 or delta.seconds > 0:
        total_days += 1 if total_days >= 0 else -1
    abs_total_days = abs(total_days)
    return abs_total_days <= DATE_UNITS["week"]

if __name__ == '__main__':
    date_a = datetime(2023, 10, 1, 10, 30, 0)
    date_b = datetime(2023, 10, 8, 10, 30, 0)
    output = is_within_one_week(date_a, date_b)
    print(output)