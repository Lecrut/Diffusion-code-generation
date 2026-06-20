from datetime import datetime, timezone, timedelta

def time_difference_in_hours(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)
    delta = abs(dt2_utc - dt1_utc)
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    dt1_sample = datetime(2023, 4, 1, 18, 0, tzinfo=timezone(timedelta(hours=-6)))
    dt2_sample = datetime(2023, 4, 1, 15, 0, tzinfo=timezone.utc)
    print(time_difference_in_hours(dt1_sample, dt2_sample))