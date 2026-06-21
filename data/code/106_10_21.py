from datetime import datetime

MONTHS_IN_YEAR = 12
DAYS_IN_COMMON_YEAR = 365
DAYS_IN_LEAP_YEAR = 366

def get_days_in_year(year: int) -> int:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return DAYS_IN_LEAP_YEAR
            return DAYS_IN_COMMON_YEAR
        return DAYS_IN_LEAP_YEAR
    return DAYS_IN_COMMON_YEAR

def get_days_in_month(month: int, year: int) -> int:
    if month == 2:
        return 29 if get_days_in_year(year) == DAYS_IN_LEAP_YEAR else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    current_date = start_date
    years_elapsed = 0
    
    while current_date.replace(year=current_date.year + 1) <= end_date:
        current_date = current_date.replace(year=current_date.year + 1)
        years_elapsed += 1
        
    return years_elapsed

if __name__ == '__main__':
    date_a = datetime(2000, 2, 29)
    date_b = datetime(2024, 2, 28)
    diff = calculate_year_difference(date_a, date_b)
    print(diff)