from datetime import datetime, timezone

def unix_timestamp_to_iso(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    result = unix_timestamp_to_iso(1609459200)
    print(result)
    result2 = unix_timestamp_to_to_iso(0)
    print(result2)
    result3 = unix_timestamp_to_iso(1700000000)
    print(result3)