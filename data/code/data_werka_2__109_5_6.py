import calendar
from datetime import datetime

def get_remaining_minutes_in_month():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    
    remaining_days = last_day - current_day
    remaining_hours_in_current_day = 23 - current_hour
    remaining_minutes_in_current_day = 59 - current_minute
    remaining_seconds_in_current_day = 59 - current_second
    
    total_remaining_minutes = (remaining_days * 24 * 60) + (remaining_hours_in_current_day * 60) + remaining_minutes_in_current_day
    
    if remaining_seconds_in_current_day > 0:
        total_remaining_minutes += 1
        
    return total_remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_month()
    print(result)