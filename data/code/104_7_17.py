from datetime import datetime, timedelta, timezone

HOURS_TO_SECONDS = 3600

def time_difference_in_hours(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    
    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)
    
    delta = dt2_utc - dt1_utc
    return delta.total_seconds() / HOURS_TO_SECONDS

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 9, 0, tzinfo=timezone(timedelta(hours=-5)))
    print(time_difference_in_hours(dt1, dt2))