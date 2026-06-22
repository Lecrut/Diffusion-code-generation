from datetime import datetime, timezone

def convert_unix_timestamp_to_iso8601(unix_timestamp: int) -> str:
    dt = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    timestamp = 1609459200
    result = convert_unix_timestamp_to_iso8601(timestamp)
    print(result)