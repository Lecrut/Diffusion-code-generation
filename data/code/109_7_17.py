import calendar
import time

def get_seconds_left_in_month():
    now = time.time()
    local = time.localtime(now)
    year = local.tm_year
    month = local.tm_mon
    last_day = calendar.monthrange(year, month)[1]
    end_timestamp = time.mktime((year, month, last_day, 23, 59, 59, 0, 0, 0))
    return end_timestamp - now

if __name__ == '__main__':
    sample_time = time.mktime((2023, 10, 15, 10, 30, 45, 0, 0, 0))
    original_time = time.time
    time.time = lambda: sample_time
    remaining = get_seconds_left_in_month()
    print(remaining)
    time.time = original_time