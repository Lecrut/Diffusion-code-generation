import datetime

def get_remaining_minutes_in_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    if month == 12:
        next_month_year = year + 1
        next_month = 1
    else:
        next_month_year = year
        next_month = month + 1
    
    first_day_next_month = datetime.datetime(next_month_year, next_month, 1)
    last_day_current_month = first_day_next_month - datetime.timedelta(days=1)
    
    end_of_current_month = datetime.datetime(year, month, last_day_current_month.day, 23, 59, 59)
    
    remaining_seconds = (end_of_current_month - now).total_seconds()
    
    if remaining_seconds < 0:
        return 0
    
    remaining_minutes = int(remaining_seconds // 60)
    
    return remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_month()
    print(result)