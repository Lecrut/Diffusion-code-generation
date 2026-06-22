import datetime
import time

RFC2822_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
RFC2822_MONTHS = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
)
OFFSET_SECONDS_PER_HOUR = 3600

def format_rfc2822(dt: datetime.datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    timestamp = dt.timestamp()
    local_time = time.gmtime(timestamp)
    day_index = local_time.tm_wday
    month_index = local_time.tm_mon - 1
    day_str = RFC2822_DAYS[day_index]
    month_str = RFC2822_MONTHS[month_index]
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    year = local_time.tm_year
    offset_seconds = dt.utcoffset().total_seconds()
    if offset_seconds >= 0:
        sign = "+"
        offset_seconds = offset_seconds
    else:
        sign = "-"
        offset_seconds = abs(offset_seconds)
    offset_hours = int(offset_seconds // OFFSET_SECONDS_PER_HOUR)
    offset_minutes = int((offset_seconds % OFFSET_SECONDS_PER_HOUR) // 60)
    offset_str = f"{sign}{offset_hours:02d}{offset_minutes:02d}"
    return f"{day_str}, {local_time.tm_mday:02d} {month_str} {year} {hour:02d}:{minute:02d}:{second:02d} {offset_str}"

if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 5, 14, 30, 0, tzinfo=datetime.timezone.utc),
        datetime.datetime(2023, 10, 5, 14, 30, 0),
        datetime.datetime(1970, 1, 1, 0, 0, 1, tzinfo=datetime.timezone.utc),
    ]
    for d in sample_dates:
        print(format_rfc2822(d))