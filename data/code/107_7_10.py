import datetime

def timestamp_to_date(timestamp):
    try:
        dt_object = datetime.datetime.utcfromtimestamp(timestamp)
        return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')
    except (TypeError, ValueError) as e:
        raise ValueError("Invalid timestamp") from e

if __name__ == '__main__':
    ts1 = 1633072800
    date_str1 = timestamp_to_date(ts1)
    print(f"{ts1}: {date_str1}")
    
    ts2 = 946684800
    date_str2 = timestamp_to_date(ts2)
    print(f"{ts2}: {date_str2}")