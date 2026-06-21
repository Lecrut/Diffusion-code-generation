import datetime
import time

def get_fractional_day_seconds(target_dt=None):
    if target_dt is None:
        target_dt = datetime.datetime.now()
    if not isinstance(target_dt, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    start_of_day = target_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = target_dt - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 12, 30, 45, 123456)
    result = get_fractional_day_seconds(sample_time)
    print(result)