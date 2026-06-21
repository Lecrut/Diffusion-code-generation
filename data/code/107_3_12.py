import email.utils
from datetime import datetime, timezone

def format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return email.utils.format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc),
        datetime(2023, 10, 5, 14, 30, 0),
        datetime(1970, 1, 1, 0, 0, 1, tzinfo=timezone.utc),
    ]
    for dt in sample_dates:
        print(format_rfc2822(dt))