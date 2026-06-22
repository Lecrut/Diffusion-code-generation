import time
import calendar

def compute_seconds_remaining_in_month():
    now = time.time()
    local_time = time.localtime(now)
    year = local_time.tm_year
    month = local_time.tm_mon
    days_in_month = calendar.monthrange(year, month)[1]
    current_day = local_time.tm_mday
    current_hour = local_time.tm_hour
    current_minute = local_time.tm_min
    current_second = local_time.tm_sec
    
    seconds_elapsed_today = current_hour * 3600 + current_minute * 60 + current_second
    seconds_remaining_today = 86400 - seconds_elapsed_today
    
    days_remaining_in_month = days_in_month - current_day
    seconds_remaining_in_full_days = days_remaining_in_month * 86400
    
    total_seconds_remaining = seconds_remaining_today + seconds_remaining_in_full_days
    return total_seconds_remaining

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)