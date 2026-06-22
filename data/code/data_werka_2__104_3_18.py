from datetime import date
import sys

def get_day_count(start: date, end: date) -> int:
    if not isinstance(start, date) or not isinstance(end, date):
        raise ValueError("Arguments must be datetime.date instances")
    return (end - start).days

if __name__ == '__main__':
    base = date(2024, 11, 1)
    target = date(2024, 12, 5)
    count = get_day_count(base, target)
    print(count)