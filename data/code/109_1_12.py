import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a numeric value')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    year = time.gmtime(timestamp).tm_year
    month = time.gmtime(timestamp).tm_mon
    _, last_day = calendar.monthrange(year, month)
    last_second_of_month = time.mktime((year, month, last_day, 23, 59, 59, 0, 0, 0))
    seconds_left = last_second_of_month - timestamp
    return int(seconds_left)
if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = seconds_left_in_month(sample_timestamp)
    print(result)