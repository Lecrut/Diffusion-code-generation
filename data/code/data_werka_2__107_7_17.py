from datetime import datetime, timezone

def convert_unix_timestamp(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    sample_timestamps = [0, 1609459200, 1700000000]
    for ts in sample_timestamps:
        result = convert_unix_timestamp(ts)
        print(result)