import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    current_time = time.localtime(timestamp)
    year = current_time.tm_year
    month = current_time.tm_mon
    _, days_in_month = calendar.monthrange(year, month)
    last_day_seconds = time.mktime((year, month, days_in_month, 23, 59, 59, 0, 0, -1))
    return int(last_day_seconds - timestamp)

if __name__ == '__main__':
    now = time.time()
    result = seconds_left_in_month(now)
    print(result)