import calendar
import math

def seconds_left_in_month(timestamp: float) -> int:
    import time
    local_time = time.localtime(timestamp)
    year = local_time.tm_year
    month = local_time.tm_mon
    _, days_in_month = calendar.monthrange(year, month)
    last_day_seconds = days_in_month * 24 * 60 * 60
    current_day_seconds = (local_time.tm_mday - 1) * 24 * 60 * 60 + local_time.tm_hour * 3600 + local_time.tm_min * 60 + local_time.tm_sec
    return last_day_seconds - current_day_seconds

if __name__ == '__main__':
    now = time.time()
    result = seconds_left_in_month(now)
    print(result)