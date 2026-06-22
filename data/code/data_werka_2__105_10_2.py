from datetime import datetime
from calendar import isleap

def get_next_day(date_str: str) -> datetime:
    year_str, month_str, day_str = date_str.split('-')
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    is_leap = 1 if isleap(year) else 0
    month_days = (0, 31, 28 + is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    max_day = month_days[month]
    next_day_val = day + 1
    if next_day_val > max_day:
        next_day_val = 1
        next_month_val = month + 1
        if next_month_val > 12:
            next_month_val = 1
            next_year_val = year + 1
        else:
            next_year_val = year
    else:
        next_month_val = month
        next_year_val = year
    return datetime(next_year_val, next_month_val, next_day_val)

if __name__ == '__main__':
    sample_date = '2024-02-28'
    result = get_next_day(sample_date)
    print(result)