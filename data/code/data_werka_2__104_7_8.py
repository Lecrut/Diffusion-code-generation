from datetime import datetime, timezone, timedelta

def compute_time_delta_hours(start_dt: datetime, end_dt: datetime) -> float:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    normalized_start = start_dt.astimezone(timezone.utc)
    normalized_end = end_dt.astimezone(timezone.utc)
    time_difference = normalized_end - normalized_start
    seconds_count = time_difference.total_seconds()
    hours_count = seconds_count / 3600
    return hours_count

if __name__ == '__main__':
    tz_offset = timezone(timedelta(hours=5))
    dt_start = datetime(2024, 6, 15, 10, 0, 0, tzinfo=tz_offset)
    dt_end = datetime(2024, 6, 15, 14, 30, 0, tzinfo=tz_offset)
    delta_value = compute_time_delta_hours(dt_start, dt_end)
    print(delta_value)