from datetime import datetime, timezone

def unix_to_iso(unix_timestamp):
    return datetime.fromtimestamp(unix_timestamp, tz=timezone.utc).isoformat()

if __name__ == '__main__':
    print(unix_to_iso(1633072800))
    print(unix_to_iso(1672531200))