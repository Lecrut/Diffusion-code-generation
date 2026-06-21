from datetime import datetime, timezone

def format_unix_timestamp(timestamp: int) -> str:
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    dt = epoch + __import__('datetime').timedelta(seconds=timestamp)
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    return f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}Z"

if __name__ == '__main__':
    test_ts = 1672531200
    output = format_unix_timestamp(test_ts)
    print(output)