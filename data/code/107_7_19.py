import datetime

def timestamp_to_iso(timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(timestamp)
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    ts1 = 1633072800
    iso_date1 = timestamp_to_iso(ts1)
    print(f"{ts1}: {iso_date1}")
    
    ts2 = 946684800
    iso_date2 = timestamp_to_iso(ts2)
    print(f"{ts2}: {iso_date2}")