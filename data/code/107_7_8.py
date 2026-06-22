import datetime

def convert_unix_timestamp_to_iso(unix_timestamp):
    dt = datetime.datetime.utcfromtimestamp(unix_timestamp)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    timestamp = 1672531200
    result = convert_unix_timestamp_to_iso(timestamp)
    print(result)