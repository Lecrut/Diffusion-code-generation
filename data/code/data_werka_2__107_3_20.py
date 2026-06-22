from datetime import datetime, timezone
from email.utils import format_datetime

DAY_NAMES = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun",
}

MONTH_NAMES = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

def format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    samples = [
        datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc),
        datetime(2023, 10, 5, 14, 30, 0),
        datetime(1970, 1, 1, 0, 0, 1, tzinfo=timezone.utc),
    ]
    for d in samples:
        print(format_rfc2822(d))