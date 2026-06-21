import datetime
import time

def compute_seconds_elapsed_today(reference_datetime=None):
    if reference_datetime is None:
        reference_datetime = datetime.datetime.now()
    
    if not isinstance(reference_datetime, datetime.datetime):
        raise ValueError("reference_datetime must be a datetime instance")
    
    if reference_datetime.tzinfo is not None:
        reference_datetime = reference_datetime.replace(tzinfo=None)
    
    start_of_day = reference_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    
    delta_seconds = (reference_datetime - start_of_day).total_seconds()
    
    return delta_seconds

if __name__ == '__main__':
    sample_time = datetime.datetime(2024, 1, 15, 14, 30, 45, 500000)
    seconds_passed = compute_seconds_elapsed_today(sample_time)
    print(seconds_passed)