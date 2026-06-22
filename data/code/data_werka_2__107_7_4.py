from datetime import datetime, timezone

def convert_timestamp_to_iso(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    sample_timestamps = [0, 1609459200, 1700000000]
    for ts in sample_timestamps:
        result = convert_timestamp_to_iso(ts)
        print(result)