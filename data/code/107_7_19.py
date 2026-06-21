from datetime import datetime, timezone
import calendar

def format_unix_timestamp(ts: int) -> str:
    if not isinstance(ts, (int, float)):
        raise ValueError("Timestamp must be numeric")
    if ts < 0:
        raise ValueError("Timestamp must be non-negative")
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    samples = [0, 1609459200, 1700000000]
    for s in samples:
        print(format_unix_timestamp(s))