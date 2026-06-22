import calendar
import time

def seconds_left_in_month(timestamp: float) -> int:
    time_struct = time.gmtime(timestamp)
    year = time_struct.tm_year
    month = time_struct.tm_mon
    _, last_day = calendar.monthrange(year, month)
    days_remaining = last_day - time_struct.tm_mday
    hours_remaining = 23 - time_struct.tm_hour
    minutes_remaining = 59 - time_struct.tm_min
    seconds_remaining = 59 - time_struct.tm_sec
    total_seconds = days_remaining * 24 * 3600 + hours_remaining * 3600 + minutes_remaining * 60 + seconds_remaining
    return total_seconds
if __name__ == '__main__':
    sample_timestamp = 1673786445.0
    result = seconds_left_in_month(sample_timestamp)
    print(result)