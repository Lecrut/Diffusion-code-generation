import datetime

UNIX_EPOCH = 1970
NANOS_PER_SEC = 1_000_000_000

def timestamp_to_iso(unix_timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(unix_timestamp)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    sample_timestamps = [1633072800, 946684800]
    for ts in sample_timestamps:
        print(timestamp_to_iso(ts))