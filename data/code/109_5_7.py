import calendar
from datetime import datetime

def get_remaining_minutes_in_current_month():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    
    remaining_seconds_today = (60 - current_second)
    remaining_minutes_today = (60 - current_minute) - (1 if remaining_seconds_today == 60 else 0)
    if remaining_minutes_today < 0:
        remaining_minutes_today = 0
        
    remaining_days = last_day - current_day
    if remaining_days < 0:
        remaining_days = 0
        
    total_remaining_minutes = (remaining_days * 24 * 60) + remaining_minutes_today
    return total_remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_current_month()
    print(result)