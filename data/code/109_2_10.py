import datetime

def get_remaining_time_in_month() -> datetime.timedelta:
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    start_date = datetime.datetime(year, month, 1)
    
    if month == 12:
        end_date = datetime.datetime(year + 1, 1, 1)
    else:
        end_date = datetime.datetime(year, month + 1, 1)
        
    remaining = end_date - now
    return remaining

if __name__ == '__main__':
    result = get_remaining_time_in_month()
    print(result)