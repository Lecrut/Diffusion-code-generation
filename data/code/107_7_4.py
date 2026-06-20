import datetime

def timestamp_to_date(timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(timestamp)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    timestamp1 = 1633072800
    print(f"{timestamp1}: {timestamp_to_date(timestamp1)}")
    timestamp2 = 946684800
    print(f"{timestamp2}: {timestamp_to_date(timestamp2)}")