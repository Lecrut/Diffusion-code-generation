from datetime import datetime, timezone, timedelta
import calendar

def _format_rfc2822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    offset = dt.utcoffset()
    total_seconds = int(offset.total_seconds())
    sign = '+' if total_seconds >= 0 else '-'
    abs_seconds = abs(total_seconds)
    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    tz_str = f"{sign}{hours:02d}{minutes:02d}"
    day_name = calendar.day_abbr[dt.weekday()]
    day = dt.day
    month_name = calendar.month_abbr[dt.month]
    year = dt.year
    time_str = dt.strftime("%H:%M:%S")
    return f"{day_name}, {day:02d} {month_name} {year} {time_str} {tz_str}"

class Rfc2822Formatter:
    def __init__(self, dt: datetime):
        self.dt = dt

    def format(self) -> str:
        return _format_rfc2822(self.dt)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    formatter1 = Rfc2822Formatter(dt1)
    print(formatter1.format())

    dt2 = datetime(2024, 1, 1, 12, 0, 0)
    formatter2 = Rfc2822Formatter(dt2)
    print(formatter2.format())

    dt3 = datetime(1970, 1, 1, 0, 0, 1, tzinfo=timezone(timedelta(hours=5, minutes=30)))
    formatter3 = Rfc2822Formatter(dt3)
    print(formatter3.format())