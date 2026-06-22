from datetime import datetime, time, timedelta

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
HOURS_PER_DAY = 24
MIDNIGHT_TIME = time.min

def compute_elapsed_since_midnight(reference_time: datetime) -> str:
    if not isinstance(reference_time, datetime):
        raise ValueError("Input must be a datetime instance")
    if reference_time.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported")
    
    start_of_day = datetime.combine(reference_time.date(), MIDNIGHT_TIME)
    delta = reference_time - start_of_day
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0 or total_seconds >= SECONDS_PER_HOUR * HOURS_PER_DAY:
        raise ValueError("Time is out of bounds for the calculated day")
    
    hours = total_seconds // SECONDS_PER_HOUR
    remainder = total_seconds % SECONDS_PER_HOUR
    minutes = remainder // SECONDS_PER_MINUTE
    seconds = remainder % SECONDS_PER_MINUTE
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 11, 15, 9, 5, 30)
    formatted_time = compute_elapsed_since_midnight(sample_dt)
    print(formatted_time)