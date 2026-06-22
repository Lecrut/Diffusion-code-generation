import datetime

def compute_fractional_day_to_seconds(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    
    if not isinstance(reference_time, datetime.datetime):
        raise ValueError("reference_time must be a datetime object")
    
    midnight = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    
    if reference_time < midnight:
        raise ValueError("reference_time cannot be before midnight of its date")
    
    elapsed_delta = reference_time - midnight
    total_seconds = elapsed_delta.total_seconds()
    
    return total_seconds

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 12, 30, 45, 123456)
    seconds_passed = compute_fractional_day_to_seconds(sample_time)
    print(seconds_passed)