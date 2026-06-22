from email.utils import format_datetime
from datetime import datetime, timezone

def format_rfc2822(dt: datetime) -> str:
    return format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    dt2 = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    print(format_rfc2822(dt1))
    print(format_rfc2822(dt2))