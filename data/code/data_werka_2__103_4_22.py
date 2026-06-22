import datetime
import math

def compute_seconds_elapsed_in_day(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    if not isinstance(reference_time, datetime.datetime):
        raise ValueError("Argument must be a datetime instance")
    if reference_time.tzinfo is not None:
        raise ValueError("Timezone-aware datetime objects are not supported")
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta_seconds = (reference_time - start_of_day).total_seconds()
    return delta_seconds

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 14, 25, 30, 500000)
    elapsed = compute_seconds_elapsed_in_day(sample_time)
    print(elapsed)