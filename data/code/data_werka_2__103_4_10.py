import datetime
import time

SECONDS_PER_HOUR = 3600
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

TIME_UNITS = {
    'hour': SECONDS_PER_HOUR,
    'minute': 60,
    'second': 1,
    'microsecond': 1e-6
}

def compute_fractional_day_seconds(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    
    total_seconds = delta.total_seconds()
    return total_seconds

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 11, 15, 14, 30, 15, 500000)
    result = compute_fractional_day_seconds(sample_time)
    print(result)