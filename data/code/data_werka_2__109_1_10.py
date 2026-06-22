import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    time_struct = time.gmtime(timestamp)
    year = time_struct.tm_year
    month = time_struct.tm_mon
    last_day = calendar.monthrange(year, month)[1]
    last_day_tuple = (year, month, last_day, 23, 59, 59, 0, 0, 0)
    last_second_timestamp = time.mktime(last_day_tuple)
    seconds_left = last_second_timestamp - timestamp
    return int(seconds_left)
if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = seconds_left_in_month(sample_timestamp)
    print(result)