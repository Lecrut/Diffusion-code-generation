from email.utils import format_datetime
from datetime import datetime, timezone

def format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc),
        datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
        datetime(1999, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
    ]
    for date in sample_dates:
        print(format_rfc2822(date))