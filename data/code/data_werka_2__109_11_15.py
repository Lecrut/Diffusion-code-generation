from datetime import datetime
import calendar

def time_remaining_in_month(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.now()
    
    current_year = now.year
    current_month = now.month
    
    if year < current_year:
        raise ValueError("The specified year must be in the future")
    if year == current_year and month < current_month:
        raise ValueError("The specified month must be in the future")
    
    if year == current_year and month == current_month:
        target_start = now
    else:
        target_start = datetime(year, month, 1)
    
    last_day = calendar.monthrange(year, month)[1]
    target_end = datetime(year, month, last_day, 23, 59, 59, 999999)
    
    remaining = target_end - target_start
    
    total_seconds = int(remaining.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)