from datetime import date
from typing import Tuple

def _validate_dates(d1: date, d2: date) -> Tuple[date, date]:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    if d1 == d2:
        raise ValueError("Dates must be distinct")
    return d1, d2

def calculate_year_difference(date1: date, date2: date) -> int:
    d1, d2 = _validate_dates(date1, date2)
    year_diff = d1.year - d2.year
    month_diff = d1.month - d2.month
    day_diff = d1.day - d2.day
    if year_diff > 0:
        if month_diff < 0 or (month_diff == 0 and day_diff < 0):
            return year_diff - 1
    elif year_diff < 0:
        if month_diff > 0 or (month_diff == 0 and day_diff > 0):
            return year_diff + 1
    return year_diff

if __name__ == '__main__':
    start_date = date(1990, 1, 1)
    end_date = date(2023, 12, 31)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)