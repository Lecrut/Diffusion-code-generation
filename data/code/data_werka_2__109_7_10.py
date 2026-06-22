import time
import calendar

def compute_seconds_remaining_in_month():
    now = time.time()
    current_time = time.localtime(now)
    year = current_time.tm_year
    month = current_time.tm_mon
    days_in_month = calendar.monthrange(year, month)[1]
    current_day = current_time.tm_mday
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec
    seconds_elapsed_today = current_hour * 3600 + current_minute * 60 + current_second
    seconds_remaining_today = 86400 - seconds_elapsed_today
    days_remaining = days_in_month - current_day
    total_seconds_remaining = seconds_remaining_today + (days_remaining * 86400)
    return total_seconds_remaining

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)