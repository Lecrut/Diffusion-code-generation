import datetime

def compute_seconds_since_midnight(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = compute_seconds_since_midnight(sample_time)
    print(result)