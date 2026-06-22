from datetime import datetime, timezone
import pytz

def compute_hour_difference(dt_start: datetime, dt_end: datetime) -> float:
    if dt_start.tzinfo is None:
        raise ValueError("Start datetime must be timezone-aware")
    if dt_end.tzinfo is None:
        raise ValueError("End datetime must be timezone-aware")
    
    dt_start_utc = dt_start.astimezone(timezone.utc)
    dt_end_utc = dt_end.astimezone(timezone.utc)
    
    diff = dt_end_utc - dt_start_utc
    seconds = diff.total_seconds()
    
    return seconds / 3600.0

if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    
    start_time = tz_ny.localize(datetime(2023, 6, 15, 10, 0, 0))
    end_time = tz_london.localize(datetime(2023, 6, 15, 15, 0, 0))
    
    hours_diff = compute_hour_difference(start_time, end_time)
    print(hours_diff)