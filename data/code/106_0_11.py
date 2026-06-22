from datetime import date
import calendar

YEARS_IN_CENTURY = 100
DAYS_IN_COMMON_YEAR = 365
DAYS_IN_LEAP_YEAR = 366

def compute_year_span(start: date, end: date) -> int:
    if start > end:
        start, end = end, start
    
    years = end.year - start.year
    
    month_day_start = (start.month, start.day)
    month_day_end = (end.month, end.day)
    
    if month_day_end < month_day_start:
        years -= 1
        
    return years

def get_days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    d1 = date(2010, 2, 28)
    d2 = date(2023, 3, 1)
    span = compute_year_span(d1, d2)
    print(span)