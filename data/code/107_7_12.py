from datetime import datetime, timezone

def unix_to_iso(unix_timestamp):
    dt_object = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    return dt_object.isoformat()

if __name__ == '__main__':
    sample_timestamps = [1633072800, 1609459200]
    for ts in sample_timestamps:
        print(unix_to_iso(ts))