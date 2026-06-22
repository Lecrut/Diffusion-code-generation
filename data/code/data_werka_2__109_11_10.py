from datetime import datetime, timedelta

def time_remaining_in_month(year: int, month: int) -> dict:
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1)
    else:
        end_date = datetime(year, month + 1, 1)
    
    now = datetime.now()
    
    if now >= end_date:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    if now < start_date:
        remaining_seconds = (end_date - start_date).total_seconds()
    else:
        remaining_seconds = (end_date - now).total_seconds()
    
    total_seconds = int(remaining_seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)