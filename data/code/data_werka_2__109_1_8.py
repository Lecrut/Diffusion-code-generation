import calendar
import time

def seconds_left_in_current_month(timestamp: float) -> int:
    current_time = time.gmtime(timestamp)
    year = current_time.tm_year
    month = current_time.tm_mon
    _, days_in_month = calendar.monthrange(year, month)
    last_day_of_month = time.mktime((year, month, days_in_month, 23, 59, 59, 0, 0, -1))
    return int(last_day_of_month - timestamp)

if __name__ == '__main__':
    sample_timestamp = time.time()
    result = seconds_left_in_current_month(sample_timestamp)
    print(result)