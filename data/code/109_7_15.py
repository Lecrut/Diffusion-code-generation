import calendar
import datetime

MONTH_DAYS_MAP = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def get_seconds_remaining_in_current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_month = 29 if is_leap else 28
    else:
        days_in_month = MONTH_DAYS_MAP[month]
    
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    
    seconds_elapsed_today = current_hour * 3600 + current_minute * 60 + current_second
    seconds_remaining_today = 86400 - seconds_elapsed_today
    
    days_remaining = days_in_month - current_day
    total_seconds_remaining = seconds_remaining_today + (days_remaining * 86400)
    
    return total_seconds_remaining

if __name__ == '__main__':
    result = get_seconds_remaining_in_current_month()
    print(result)