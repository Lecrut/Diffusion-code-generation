import datetime

def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')

if __name__ == '__main__':
    sample_timestamp = 1633024800
    print(timestamp_to_date(sample_timestamp))