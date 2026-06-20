import datetime

def timestamp_to_iso(unix_timestamp):
    try:
        dt_object = datetime.datetime.utcfromtimestamp(unix_timestamp)
        return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')
    except (TypeError, ValueError) as e:
        raise ValueError("Invalid Unix timestamp") from e

if __name__ == '__main__':
    timestamp1 = 1633072800
    print(timestamp_to_iso(timestamp1))
    timestamp2 = 946684800
    print(timestamp_to_iso(timestamp2))