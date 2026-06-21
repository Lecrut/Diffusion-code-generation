from datetime import datetime, timedelta

def get_remaining_time_in_month() -> timedelta:
    start_date = datetime(2023, 10, 1)
    end_date = datetime(2023, 10, 31)
    now = datetime(2023, 10, 15, 12, 0, 0)
    
    if now < start_date:
        remaining = end_date - start_date
    elif now > end_date:
        remaining = timedelta(0)
    else:
        remaining = end_date - now
        
    return remaining

if __name__ == '__main__':
    result = get_remaining_time_in_month()
    print(result)