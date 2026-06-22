import datetime
import time

SECONDS_IN_HOUR = 3600
MINUTES_IN_HOUR = 60

def compute_fractional_day_seconds(year, month, day, hour, minute, second, microsecond=0):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Date components must be integers")
    if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
        raise ValueError("Time components must be integers")
    if not isinstance(microsecond, int):
        raise ValueError("Microsecond component must be an integer")
    
    try:
        current_time = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    except ValueError as e:
        raise ValueError(f"Invalid date or time provided: {e}")
    
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = current_time - start_of_day
    return elapsed.total_seconds()

if __name__ == '__main__':
    now = datetime.datetime.now()
    result = compute_fractional_day_seconds(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        now.microsecond
    )
    print(result)