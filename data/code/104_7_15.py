from datetime import datetime

def time_difference_in_hours(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    return (dt2.astimezone(dt1.tzinfo) - dt1).total_seconds() / 3600

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 9, 0, tzinfo=timezone(timedelta(hours=-5)))
    print(time_difference_in_hours(dt1, dt2))