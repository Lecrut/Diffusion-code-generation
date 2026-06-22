from datetime import datetime, timezone

def unix_timestamp_to_iso(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    print(unix_timestamp_to_iso(1672531200))
    print(unix_timestamp_to_to_iso(0))
    print(unix_timestamp_to_iso(1704067200))