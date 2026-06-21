import datetime
import calendar

def time_remaining_in_month(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.datetime.now()
    target_month_start = datetime.datetime(year, month, 1)
    target_month_end = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    
    if now > target_month_end:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    delta = target_month_end - now
    total_seconds = int(delta.total_seconds())
    
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)