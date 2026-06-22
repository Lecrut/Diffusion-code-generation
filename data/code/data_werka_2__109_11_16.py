import datetime

def time_remaining_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    first_day = datetime.date(year, month, 1)
    if month == 12:
        last_day = datetime.date(year + 1, 1, 1)
    else:
        last_day = datetime.date(year, month + 1, 1)
    
    now = datetime.datetime.now()
    start_of_month = datetime.datetime(year, month, 1)
    end_of_month = last_day
    
    if now < start_of_month:
        total_seconds = (end_of_month - start_of_month).total_seconds()
    elif now > end_of_month:
        total_seconds = 0
    else:
        remaining = end_of_month - now
        total_seconds = remaining.total_seconds()
    
    total_seconds = int(total_seconds)
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)