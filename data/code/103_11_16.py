from datetime import datetime

def calculate_elapsed_time_today():
    now = datetime.now()
    if not isinstance(now, datetime):
        raise ValueError("Invalid input type for current time")
    
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_seconds = (now - start_of_day).total_seconds()
    return int(elapsed_seconds)

if __name__ == '__main__':
    elapsed = calculate_elapsed_time_today()
    print(elapsed)