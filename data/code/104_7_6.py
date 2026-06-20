from datetime import datetime, timedelta, timezone

def validate_datetime(dt):
    if dt.tzinfo is None:
        raise ValueError("Datetime object must be timezone-aware")

def time_difference_in_hours(dt1, dt2):
    validate_datetime(dt1)
    validate_datetime(dt2)
    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)
    delta = abs(dt2_utc - dt1_utc)
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 9, 0, tzinfo=timezone(timedelta(hours=-5)))
    print(time_difference_in_hours(dt1, dt2))