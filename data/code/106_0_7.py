from datetime import date
from typing import Tuple

MONTH_DAYS: dict[int, int] = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_year(year: int) -> int:
    return 366 if is_leap_year(year) else 365

def _days_between_dates(d1: date, d2: date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    total_days = 0
    current_year = d1.year
    while current_year < d2.year:
        total_days += days_in_year(current_year)
        current_year += 1
    total_days += (d2.toordinal() - d1.toordinal())
    return total_days

def calculate_year_difference(start_date: date, end_date: date) -> float:
    if start_date == end_date:
        return 0.0
    total_days = _days_between_dates(start_date, end_date)
    average_days_per_year = 365.2425
    return total_days / average_days_per_year

if __name__ == '__main__':
    start = date(2020, 2, 29)
    end = date(2024, 2, 28)
    diff = calculate_year_difference(start, end)
    print(diff)