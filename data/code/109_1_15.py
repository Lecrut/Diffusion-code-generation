import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    current_time = time.localtime(timestamp)
    year = current_time.tm_year
    month = current_time.tm_mon
    _, days_in_month = calendar.monthrange(year, month)
    last_day_seconds = days_in_month * 24 * 3600
    current_day_seconds = current_time.tm_mday * 24 * 3600
    current_hour_seconds = current_time.tm_hour * 3600
    current_minute_seconds = current_time.tm_min * 60
    current_second_seconds = current_time.tm_sec
    elapsed_seconds = current_day_seconds + current_hour_seconds + current_minute_seconds + current_second_seconds
    remaining_seconds = last_day_seconds - elapsed_seconds
    return remaining_seconds

if __name__ == '__main__':
    now = time.time()
    result = seconds_left_in_month(now)
    print(result)