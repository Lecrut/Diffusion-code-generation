from datetime import datetime, timezone, timedelta
import calendar

DAY_NAMES = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
MONTH_NAMES = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

def format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    days = DAY_NAMES[dt.weekday()]
    month = MONTH_NAMES[dt.month]
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    year = dt.year
    
    offset_seconds = dt.utcoffset().total_seconds()
    sign = '+' if offset_seconds >= 0 else '-'
    offset_seconds = abs(int(offset_seconds))
    offset_hours, offset_mins = divmod(offset_seconds, 3600)
    
    return f"{days}, {dt.day:02d} {month} {year} {hour:02d}:{minute:02d}:{second:02d} {sign}{offset_hours:02d}{offset_mins:02d}"

if __name__ == '__main__':
    samples = {
        'utc_now_like': datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc),
        'naive_treated_as_utc': datetime(2024, 1, 1, 0, 0, 0),
        'positive_offset': datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone(timedelta(hours=5))),
        'negative_offset': datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone(timedelta(hours=-8)))
    }
    for name, d in samples.items():
        print(format_rfc2822(d))