from datetime import datetime
from calendar import monthrange

MONTHS_PER_YEAR = 12
DAYS_PER_MONTH_LOOKUP = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def get_full_years_between(start: datetime, end: datetime) -> int:
    if end < start:
        start, end = end, start
    
    years_diff = end.year - start.year
    
    if years_diff == 0:
        return 0
    
    end_day_in_month = end.day
    end_month = end.month
    start_day_in_month = start.day
    start_month = start.month
    
    start_max_days = DAYS_PER_MONTH_LOOKUP.get(start_month, 30)
    if start_month == 2:
        is_leap = (start.year % 4 == 0 and start.year % 100 != 0) or (start.year % 400 == 0)
        if is_leap:
            start_max_days = 29
            
    end_max_days = DAYS_PER_MONTH_LOOKUP.get(end_month, 30)
    if end_month == 2:
        is_leap = (end.year % 4 == 0 and end.year % 100 != 0) or (end.year % 400 == 0)
        if is_leap:
            end_max_days = 29
            
    month_diff = (end_month - start_month)
    day_diff = end_day_in_month - start_day_in_month
    
    if month_diff < 0 or (month_diff == 0 and day_diff < 0):
        years_diff -= 1
        
    return years_diff

if __name__ == '__main__':
    dt_start = datetime(2018, 3, 15)
    dt_end = datetime(2024, 3, 14)
    diff = get_full_years_between(dt_start, dt_end)
    print(diff)