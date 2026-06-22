from datetime import datetime, timezone, timedelta

def compute_hour_difference(dt_start: datetime, dt_end: datetime) -> float:
    if not hasattr(dt_start, 'tzinfo') or dt_start.tzinfo is None:
        raise ValueError("Start datetime must be timezone-aware")
    if not hasattr(dt_end, 'tzinfo') or dt_end.tzinfo is None:
        raise ValueError("End datetime must be timezone-aware")
    offset_seconds = (dt_end - dt_start).total_seconds()
    return offset_seconds / 3600

if __name__ == '__main__':
    utc = timezone.utc
    start_time = datetime(2023, 11, 15, 8, 0, 0, tzinfo=utc)
    end_time = datetime(2023, 11, 15, 14, 30, 0, tzinfo=utc)
    diff = compute_hour_difference(start_time, end_time)
    print(diff)