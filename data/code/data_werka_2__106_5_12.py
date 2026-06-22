from datetime import date
from typing import Tuple

def _validate_date(d: date) -> None:
    if not isinstance(d, date):
        raise ValueError("Input must be a date object")
    if d.year < 1 or d.year > 9999:
        raise ValueError("Year out of valid range")

def _compute_year_span(d1: date, d2: date) -> int:
    _validate_date(d1)
    _validate_date(d2)
    return abs(d1.year - d2.year)

def calculate_year_difference(date1: date, date2: date) -> int:
    return _compute_year_span(date1, date2)

if __name__ == '__main__':
    start_date = date(1995, 12, 31)
    end_date = date(2023, 1, 1)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)