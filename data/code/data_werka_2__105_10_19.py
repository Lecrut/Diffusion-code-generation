from datetime import datetime, timedelta

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def get_next_day(date_str: str) -> datetime:
    current_dt = datetime.strptime(date_str, '%Y-%m-%d')
    year = current_dt.year
    month = current_dt.month
    day = current_dt.day
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_days = DAYS_IN_MONTH[month]
    if month == 2 and is_leap:
        max_days = 29
    
    if day < max_days:
        next_dt = current_dt.replace(day=day + 1)
    elif month < 12:
        next_dt = current_dt.replace(year=year, month=month + 1, day=1)
    else:
        next_dt = current_dt.replace(year=year + 1, month=1, day=1)
    
    return next_dt

if __name__ == '__main__':
    sample_date = '2024-02-28'
    result = get_next_day(sample_date)
    print(result)