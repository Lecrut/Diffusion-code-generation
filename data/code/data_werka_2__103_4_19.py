import datetime
import time

def compute_seconds_in_fractional_day(year, month, day, hour, minute, second, microsecond=0):
    target_time = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    midnight = target_time.replace(hour=0, minute=0, second=0, microsecond=0)
    time_delta = target_time - midnight
    elapsed = time_delta.total_seconds()
    return elapsed

if __name__ == '__main__':
    y = 2024
    m = 6
    d = 15
    h = 14
    mi = 25
    s = 30
    us = 500000
    sample = datetime.datetime(y, m, d, h, mi, s, us)
    result = compute_seconds_in_fractional_day(
        sample.year,
        sample.month,
        sample.day,
        sample.hour,
        sample.minute,
        sample.second,
        sample.microsecond
    )
    print(result)