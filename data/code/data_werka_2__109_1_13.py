import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a number')
    time_struct = time.gmtime(timestamp)
    year = time_struct.tm_year
    month = time_struct.tm_mon
    last_day = calendar.monthrange(year, month)[1]
    if month == 12:
        next_month_year = year + 1
        next_month = 1
    else:
        next_month_year = year
        next_month = month + 1
    next_month_start = time.mktime((next_month_year, next_month, 1, 0, 0, 0, 0, 0, 0))
    seconds_left = next_month_start - timestamp
    return int(seconds_left)
if __name__ == '__main__':
    sample_timestamp = 1705320000
    result = seconds_left_in_month(sample_timestamp)
    print(result)