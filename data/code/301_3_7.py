from datetime import datetime

def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d-%b-%Y %H:%M:%S')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_datetime(sample_timestamp))