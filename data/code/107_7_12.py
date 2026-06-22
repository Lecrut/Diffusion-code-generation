import calendar
from datetime import datetime, timezone

def format_unix_timestamp(ts: int) -> str:
    if not isinstance(ts, (int, float)):
        raise ValueError("Timestamp must be a number")
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    print(format_unix_timestamp(0))
    print(format_unix_timestamp(1609459200))
    print(format_unix_timestamp(1700000000))