from datetime import date
from typing import Union

def _validate_date_input(obj: object) -> bool:
    return isinstance(obj, date)

def _compute_delta_days(start: date, end: date) -> int:
    return (end - start).days

def calculate_days_difference(first_date: date, second_date: date) -> int:
    if not _validate_date_input(first_date):
        raise ValueError("first_date must be a date object")
    if not _validate_date_input(second_date):
        raise ValueError("second_date must be a date object")
    return _compute_delta_days(first_date, second_date)

if __name__ == '__main__':
    date_a = date(2021, 5, 10)
    date_b = date(2021, 6, 15)
    days_diff = calculate_days_difference(date_a, date_b)
    print(days_diff)