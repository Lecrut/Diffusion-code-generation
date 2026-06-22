import datetime
import sys

def get_delta_hours(dt1: datetime.datetime, dt2: datetime.datetime) -> float:
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    delta = dt2 - dt1
    return delta.total_seconds() / 3600.0

if __name__ == '__main__':
    tz = datetime.timezone.utc
    dt1 = datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=tz)
    dt2 = datetime.datetime(2023, 1, 1, 15, 30, 0, tzinfo=tz)
    result = get_delta_hours(dt1, dt2)
    print(result)