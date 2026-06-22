from datetime import datetime, timedelta

def time_remaining_in_month(year: int, month: int) -> dict:
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    
    now = datetime.now()
    
    if now >= end:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    if now < start:
        remaining = end - start
    else:
        remaining = end - now
    
    total_seconds = int(remaining.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)