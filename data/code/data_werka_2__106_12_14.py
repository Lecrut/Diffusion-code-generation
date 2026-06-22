from datetime import date
from typing import Tuple

def get_years_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    year_diff: int = end_date.year - start_date.year
    month_diff: int = end_date.month - start_date.month
    day_diff: int = end_date.day - start_date.day
    
    if year_diff == 0:
        return 0
    
    if month_diff < 0:
        return year_diff - 1
    
    if month_diff == 0 and day_diff < 0:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    d_start: date = date(1990, 2, 28)
    d_end: date = date(2024, 2, 27)
    years: int = get_years_difference(d_start, d_end)
    print(years)