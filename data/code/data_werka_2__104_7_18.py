from datetime import datetime, timezone, timedelta

def get_delta_hours(dt1: datetime, dt2: datetime) -> float:
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    
    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)
    
    delta = dt1_utc - dt2_utc
    total_seconds = delta.total_seconds()
    
    return total_seconds / 3600

if __name__ == '__main__':
    tz = timezone(timedelta(hours=5))
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=tz)
    dt2 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    
    result = get_delta_hours(dt1, dt2)
    print(result)