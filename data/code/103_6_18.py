import datetime
import time

def get_seconds_elapsed_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    total_seconds = delta.total_seconds()
    if total_seconds < 0 or total_seconds >= 86400:
        raise ValueError("Time delta out of expected range for a single day")
    return total_seconds

if __name__ == '__main__':
    sample_time_offset = 0
    base_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    sample_current = base_midnight + datetime.timedelta(seconds=3600)
    sample_midnight = sample_current.replace(hour=0, minute=0, second=0, microsecond=0)
    sample_delta = sample_current - sample_midnight
    sample_result = sample_delta.total_seconds()
    print(sample_result)
    actual_result = get_seconds_elapsed_since_midnight()
    print(actual_result)