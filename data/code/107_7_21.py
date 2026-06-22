from datetime import datetime, timezone
import calendar

def format_unix_timestamp(timestamp: int) -> str:
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    year, month, day, hour, minute, second = calendar.gmtime(timestamp)[:6]
    
    return f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}Z"

if __name__ == '__main__':
    print(format_unix_timestamp(0))
    print(format_unix_timestamp(1609459200))
    print(format_unix_timestamp(1700000000))