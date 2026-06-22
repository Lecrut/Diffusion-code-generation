from datetime import datetime, timezone
from email.utils import format_datetime as _format_datetime

class Rfc2822Formatter:
    def __init__(self, default_tz: timezone = None):
        self.default_tz = default_tz

    def format(self, dt: datetime) -> str:
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=self.default_tz or timezone.utc)
        return _format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    formatter = Rfc2822Formatter()
    dt1 = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    dt2 = datetime(2024, 1, 1, 12, 0, 0)
    print(formatter.format(dt1))
    print(formatter.format(dt2))