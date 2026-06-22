from datetime import datetime, timezone
from calendar import timegm

class RFC2822Formatter:
    def __init__(self, default_tz: timezone = None):
        self.default_tz = default_tz or timezone.utc

    def format(self, dt: datetime) -> str:
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=self.default_tz)
        offset = dt.utcoffset()
        total_seconds = int(offset.total_seconds())
        sign = '+' if total_seconds >= 0 else '-'
        hours, remainder = divmod(abs(total_seconds) // 60, 60)
        tz_str = f'{sign}{hours:02d}{remainder:02d}'
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        day_name = days[dt.weekday()]
        day = dt.day
        month = month_names[dt.month - 1]
        year = dt.year
        time_part = f'{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}'
        return f'{day_name}, {day:02d} {month} {year} {time_part} {tz_str}'

if __name__ == '__main__':
    formatter = RFC2822Formatter()
    dt1 = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    dt2 = datetime(2024, 1, 1, 0, 0, 0)
    dt3 = datetime(1999, 12, 31, 23, 59, 59, tzinfo=timezone(timedelta(hours=5)))
    from datetime import timedelta
    dt3 = datetime(1999, 12, 31, 23, 59, 59, tzinfo=timezone(timedelta(hours=5)))
    print(formatter.format(dt1))
    print(formatter.format(dt2))
    print(formatter.format(dt3))