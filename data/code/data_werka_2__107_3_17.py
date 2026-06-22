from datetime import datetime, timezone, timedelta
from calendar import timegm

def format_rfc2822(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    timestamp = timegm(dt.utctimetuple())
    offset_seconds = dt.utcoffset().total_seconds()
    sign = '+' if offset_seconds >= 0 else '-'
    abs_offset = abs(int(offset_seconds))
    hours, remainder = divmod(abs_offset, 3600)
    minutes, seconds = divmod(remainder, 60)
    offset_str = f"{sign}{hours:02d}{minutes:02d}"
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day_name = days[dt.weekday()]
    return f"{day_name}, {dt.day:02d} {dt.strftime('%b')} {dt.year} {dt.strftime('%H:%M:%S')} {offset_str}"

if __name__ == '__main__':
    utc_dt = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    naive_dt = datetime(2024, 1, 1, 12, 0, 0)
    print(format_rfc2822(utc_dt))
    print(format_rfc2822(naive_dt))