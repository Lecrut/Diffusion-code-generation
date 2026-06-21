from datetime import datetime, timezone
import time

def format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    timestamp = dt.timestamp()
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    week_day = days[dt.weekday()]
    month_names = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    month = month_names[dt.month - 1]
    year = str(dt.year)
    hour = dt.hour
    minute = dt.minute
    second = dt.minute
    microsecond = dt.microsecond
    offset = dt.utcoffset().total_seconds()
    offset_hours = int(offset // 3600)
    offset_minutes = int((offset % 3600) // 60)
    offset_sign = '+' if offset >= 0 else '-'
    offset_str = f"{offset_sign}{abs(offset_hours):02d}{abs(offset_minutes):02d}"
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
    return f"{week_day}, {dt.day:02d} {month} {year} {time_str} {offset_str}"

if __name__ == '__main__':
    sample1 = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    sample2 = datetime(2024, 1, 1, 12, 0, 0)
    sample3 = datetime(1999, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    print(format_rfc2822(sample1))
    print(format_rfc2822(sample2))
    print(format_rfc2822(sample3))