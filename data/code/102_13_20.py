from datetime import date
from datetime import datetime

def is_weekday(d: date) -> bool:
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise ValueError("Input must be a date object")
    return d.weekday() < 5

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        datetime(2023, 10, 24, 12, 0, 0),
    ]
    for t in test_cases:
        print(is_weekday(t))