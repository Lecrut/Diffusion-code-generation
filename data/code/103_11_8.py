import datetime

def calculate_elapsed_time_today():
    now = datetime.datetime.now()
    if not isinstance(now, datetime.datetime):
        raise ValueError("Expected current time to be a datetime object")
    
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if not isinstance(start_of_day, datetime.datetime):
        raise ValueError("Expected start of day to be a datetime object")
    
    elapsed_seconds = (now - start_of_day).total_seconds()
    if not isinstance(elapsed_seconds, (int, float)):
        raise ValueError("Expected elapsed time to be an integer or float")
    
    return int(elapsed_seconds)

if __name__ == '__main__':
    elapsed = calculate_elapsed_time_today()
    print(elapsed)