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
    
    if current_date == end_date:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    days_remaining = (end_date - current_date).days
    hours_remaining = days_remaining * 24 - current_time.hour
    minutes_remaining = hours_remaining * 60 - current_time.minute
    seconds_remaining = minutes_remaining * 60 - current_time.second
    
    if seconds_remaining < 0:
        seconds_remaining += 60
        minutes_remaining -= 1
    
    if minutes_remaining < 0:
        minutes_remaining += 60
        hours_remaining -= 1
    
    if hours_remaining < 0:
        hours_remaining = 0
        minutes_remaining = 0
        seconds_remaining = 0
    
    return {"hours": hours_remaining, "minutes": minutes_remaining, "seconds": seconds_remaining}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)