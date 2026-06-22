from datetime import datetime

def is_valid_timestamp(timestamp):
    return isinstance(timestamp, int) and timestamp >= 0

def timestamp_to_human_readable(timestamp):
    if not is_valid_timestamp(timestamp):
        raise ValueError("Invalid timestamp")
    return datetime.fromtimestamp(timestamp).strftime('%d-%b-%Y %H:%M:%S')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_human_readable(sample_timestamp))