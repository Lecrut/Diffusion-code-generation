import calendar
from datetime import datetime, timezone

def format_unix_timestamp_to_iso(timestamp: int) -> str:
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be a number")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    if not (isinstance(timestamp, int) or timestamp.is_integer()):
        raise ValueError("Timestamp must be an integer value")
    dt_object = datetime.fromtimestamp(int(timestamp), tz=timezone.utc)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    test_timestamps = [0, 1609459200, 1700000000]
    for ts in test_timestamps:
        formatted_date = format_unix_timestamp_to_iso(ts)
        print(formatted_date)