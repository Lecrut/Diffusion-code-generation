from datetime import datetime

DATE_FORMAT = '%d-%b-%Y %H:%M:%S'

def timestamp_to_human_readable(timestamp):
    return datetime.fromtimestamp(timestamp).strftime(DATE_FORMAT)

if __name__ == '__main__':
    sample_timestamps = [1633072800, 1672531200]
    for timestamp in sample_timestamps:
        print(timestamp_to_human_readable(timestamp))