import datetime
import calendar

def get_remaining_time(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    
    now = datetime.datetime.now()
    target_start = datetime.datetime(year, month, 1)
    target_end = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    
    if now > target_end:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    delta = target_end - now
    total_seconds = int(delta.total_seconds())
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = get_remaining_time(2024, 12)
    print(result)