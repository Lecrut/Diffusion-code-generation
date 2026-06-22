import datetime
import time

def compute_fractional_day_seconds(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    if not isinstance(reference_time, datetime.datetime):
        raise ValueError("reference_time must be a datetime object")
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 12, 30, 45, 123456)
    result = compute_fractional_day_seconds(sample_time)
    print(result)