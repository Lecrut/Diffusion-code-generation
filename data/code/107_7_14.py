import datetime

def timestamp_to_date(unix_timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(unix_timestamp)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    timestamp1 = 1633072800
    date_str1 = timestamp_to_date(timestamp1)
    print(f"{timestamp1}: {date_str1}")

    timestamp2 = 946684800
    date_str2 = timestamp_to_date(timestamp2)
    print(f"{timestamp2}: {date_str2}")