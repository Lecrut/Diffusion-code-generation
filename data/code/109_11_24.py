import calendar
import datetime

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
DAYS_PER_WEEK = 7

def compute_remaining_time(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    
    current = datetime.datetime.now()
    target_month_start = datetime.datetime(year, month, 1)
    
    if month == 12:
        target_month_end = datetime.datetime(year + 1, 1, 1)
    else:
        target_month_end = datetime.datetime(year, month + 1, 1)
    
    total_seconds_remaining = int((target_month_end - current).total_seconds())
    
    if total_seconds_remaining < 0:
        total_seconds_remaining = 0
        
    hours = total_seconds_remaining // SECONDS_PER_HOUR
    remainder = total_seconds_remaining % SECONDS_PER_HOUR
    minutes = remainder // SECONDS_PER_MINUTE
    seconds = remainder % SECONDS_PER_MINUTE
    
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    result = compute_remaining_time(2024, 10)
    print(result)