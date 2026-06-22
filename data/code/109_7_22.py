import time
import calendar

def compute_seconds_remaining_in_month():
    now = time.time()
    local_time = time.localtime(now)
    year = local_time.tm_year
    month = local_time.tm_mon
    _, days_in_month = calendar.monthrange(year, month)
    last_day_seconds = time.mktime((year, month, days_in_month, 23, 59, 59, 0, 0, 0))
    remaining = last_day_seconds - now
    return int(remaining)

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)