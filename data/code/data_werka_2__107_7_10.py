from datetime import datetime, timezone

SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400
EPOCH = 0
OUTPUT_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
UTC = timezone.utc

def unix_to_iso(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=UTC)
    return dt.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    ts1 = 0
    ts2 = 1609459200
    ts3 = 1700000000
    print(unix_to_iso(ts1))
    print(unix_to_iso(ts2))
    print(unix_to_iso(ts3))