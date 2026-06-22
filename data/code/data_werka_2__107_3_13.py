import email.utils
from datetime import datetime, timezone

class Rfc2822Formatter:
    def __init__(self, usegmt: bool = True):
        self._usegmt = usegmt

    def format(self, dt: datetime) -> str:
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return email.utils.format_datetime(dt, usegmt=self._usegmt)

if __name__ == '__main__':
    formatter = Rfc2822Formatter(usegmt=True)
    dt_utc = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    dt_naive = datetime(2023, 10, 5, 14, 30, 0)
    print(formatter.format(dt_utc))
    print(formatter.format(dt_naive))