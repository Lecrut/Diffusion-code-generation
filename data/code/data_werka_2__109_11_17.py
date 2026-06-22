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
    current_date = now.date()
    current_time = now.time()
    
    if current_date > last_day:
        return (0, 0, 0)
    
    if current_date == last_day:
        return (0, 0, 0)
    
    if current_date == first_day:
        remaining_seconds = (last_day - current_date).total_seconds() - (current_time.hour * 3600 + current_time.minute * 60 + current_time.second)
        if remaining_seconds < 0:
            remaining_seconds = 0
        total_seconds = int(remaining_seconds)
    else:
        days_remaining = (last_day - current_date).days
        total_seconds = days_remaining * 86400 - (current_time.hour * 3600 + current_time.minute * 60 + current_time.second)
        if total_seconds < 0:
            total_seconds = 0
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return (hours, minutes, seconds)

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 10)
    print(result)