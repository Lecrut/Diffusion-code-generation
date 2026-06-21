import datetime

def get_remaining_minutes_in_current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    if month == 12:
        next_month = datetime.datetime(year + 1, 1, 1)
    else:
        next_month = datetime.datetime(year, month + 1, 1)
    
    last_day_of_month = next_month - datetime.timedelta(days=1)
    last_day_of_month = last_day_of_month.replace(hour=23, minute=59, second=59, microsecond=0)
    
    remaining_seconds = (last_day_of_month - now).total_seconds()
    
    if remaining_seconds < 0:
        return 0
    
    remaining_minutes = int(remaining_seconds // 60)
    return remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_current_month()
    print(result)