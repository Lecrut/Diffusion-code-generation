from datetime import datetime, timezone
import calendar

def format_unix_timestamp(timestamp: int) -> str:
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be a numeric type")
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    utc_dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return utc_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    test_cases = [0, 1609459200, 1700000000, 1672531200]
    for ts in test_cases:
        formatted_date = format_unix_timestamp(ts)
        print(formatted_date)