import datetime
import calendar

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def time_remaining_in_month(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.datetime.now()
    
    target_start = datetime.datetime(year, month, 1)
    
    if month == 12:
        target_end = datetime.datetime(year + 1, 1, 1)
    else:
        target_end = datetime.datetime(year, month + 1, 1)
    
    if now >= target_end:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    if now < target_start:
        remaining_seconds = (target_end - target_start).total_seconds()
    else:
        remaining_seconds = (target_end - now).total_seconds()
    
    remaining_seconds = int(remaining_seconds)
    
    hours = remaining_seconds // SECONDS_PER_HOUR
    remaining_seconds %= SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)