from datetime import date
import sys

def compute_days_delta(first: date, second: date) -> int:
    if not isinstance(first, date):
        raise TypeError(f"first must be a date instance, got {type(first).__name__}")
    if not isinstance(second, date):
        raise TypeError(f"second must be a date instance, got {type(second).__name__}")
    total_seconds = (second - first).total_seconds()
    days = int(total_seconds // 86400)
    return days

if __name__ == '__main__':
    ref_start = date(2020, 1, 1)
    ref_end = date(2020, 1, 5)
    diff = compute_days_delta(ref_start, ref_end)
    print(diff)