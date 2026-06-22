import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
ZERO_TIME = datetime.time(0, 0, 0)

def calculate_elapsed_time_formatted(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_delta = reference_time - start_of_day
    total_seconds = int(elapsed_delta.total_seconds())
    
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_seconds = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = calculate_elapsed_time_formatted(sample_time)
    print(result)