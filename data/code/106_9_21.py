from datetime import date
import calendar

MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    if month == 2 and is_leap_year(year):
        return 29
    return MONTH_DAYS[month]

def compute_year_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        return -compute_year_difference(end_date, start_date)
    
    years = end_date.year - start_date.year
    
    if end_date.month < start_date.month:
        years -= 1
    elif end_date.month == start_date.month:
        if end_date.day < start_date.day:
            years -= 1
            
    return years

if __name__ == '__main__':
    d_start = date(2019, 11, 30)
    d_end = date(2023, 11, 30)
    diff = compute_year_difference(d_start, d_end)
    print(diff)