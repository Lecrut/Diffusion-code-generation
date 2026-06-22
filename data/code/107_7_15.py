from datetime import datetime, timezone

def unix_to_iso(timestamp: int) -> str:
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    dt = epoch + __import__('datetime').timedelta(seconds=timestamp)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    samples = {
        'epoch': 0,
        'new_year_2021': 1609459200,
        'recent': 1700000000
    }
    for name, ts in samples.items():
        print(unix_to_iso(ts))