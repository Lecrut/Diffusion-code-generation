from datetime import date
from typing import Tuple

MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year: int, month: int) -> int:
    if month == 2 and is_leap_year(year):
        return 29
    return MONTH_DAYS[month]

def calculate_year_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    years = end_date.year - start_date.year
    
    if end_date.month < start_date.month:
        years -= 1
    elif end_date.month == start_date.month:
        if end_date.day < start_date.day:
            years -= 1
            
    return years

def get_date_components(d: date) -> Tuple[int, int, int]:
    return d.year, d.month, d.day

if __name__ == '__main__':
    d1 = date(2010, 5, 15)
    d2 = date(2023, 5, 14)
    diff = calculate_year_difference(d1, d2)
    print(diff)
    d3 = date(2020, 2, 29)
    d4 = date(2021, 2, 28)
    diff2 = calculate_year_difference(d3, d4)
    print(diff2)