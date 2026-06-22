import datetime

def time_remaining_in_month(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    start_date = datetime.date(year, month, 1)
    if month == 12:
        end_date = datetime.date(year + 1, 1, 1)
    else:
        end_date = datetime.date(year, month + 1, 1)
    
    now = datetime.datetime.now()
    current_date = now.date()
    current_time = now.time()
    
    if current_date > end_date:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    if current_date == start_date:
        remaining_seconds = (end_date - current_date).total_seconds() - (current_time.hour * 3600 + current_time.minute * 60 + current_time.second)
    else:
        remaining_seconds = (end_date - current_date).total_seconds()
    
    if remaining_seconds < 0:
        remaining_seconds = 0
    
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)