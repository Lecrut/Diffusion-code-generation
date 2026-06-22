from datetime import datetime, timezone
from email.utils import format_datetime

def format_rfc2822(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc),
        datetime(2023, 10, 5, 14, 30, 0),
        datetime(1970, 1, 1, 0, 0, 1, tzinfo=timezone.utc),
    ]
    for d in sample_dates:
        print(format_rfc2822(d))