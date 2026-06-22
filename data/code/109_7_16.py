import time
import calendar

def compute_seconds_remaining_in_month():
    now = time.time()
    current_year = time.localtime(now).tm_year
    current_month = time.localtime(now).tm_mon
    last_day = calendar.monthrange(current_year, current_month)[1]
    last_day_timestamp = time.mktime((current_year, current_month, last_day, 23, 59, 59, 0, 0, 0))
    seconds_remaining = last_day_timestamp - now
    return seconds_remaining

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)