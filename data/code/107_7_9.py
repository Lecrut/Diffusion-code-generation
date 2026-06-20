import datetime
timestamp_to_date = {}

def timestamp_to_iso(unix_timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(unix_timestamp)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')
if __name__ == '__main__':
    sample_timestamps = [1633072800, 946684800]
    for timestamp in sample_timestamps:
        print(f'{timestamp}: {timestamp_to_iso(timestamp)}')