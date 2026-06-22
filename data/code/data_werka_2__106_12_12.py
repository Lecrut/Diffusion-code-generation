from datetime import date
from typing import Tuple

DAYS_IN_COMMON_YEAR: int = 365
DAYS_IN_LEAP_YEAR: int = 366
MONTH_DAYS: Tuple[int, ...] = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def compute_years_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    years_diff: int = end_date.year - start_date.year
    
    if years_diff == 0:
        return 0
    
    start_month_days: int = MONTH_DAYS[start_date.month - 1]
    if start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0):
        start_month_days += 1
    
    end_month_days: int = MONTH_DAYS[end_date.month - 1]
    if end_date.year % 4 == 0 and (end_date.year % 100 != 0 or end_date.year % 400 == 0):
        end_month_days += 1
    
    start_day_of_year: int = sum(MONTH_DAYS[:start_date.month - 1]) + start_date.day
    if start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0):
        if start_date.month > 2:
            start_day_of_year += 1
            
    end_day_of_year: int = sum(MONTH_DAYS[:end_date.month - 1]) + end_date.day
    if end_date.year % 4 == 0 and (end_date.year % 100 != 0 or end_date.year % 400 == 0):
        if end_date.month > 2:
            end_day_of_year += 1
            
    if end_day_of_year < start_day_of_year:
        years_diff -= 1
        
    return years_diff

if __name__ == '__main__':
    d_start: date = date(2000, 2, 29)
    d_end: date = date(2024, 2, 28)
    result: int = compute_years_difference(d_start, d_end)
    print(result)