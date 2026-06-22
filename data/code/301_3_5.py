from datetime import datetime

def validate_timestamp(timestamp):
    if not isinstance(timestamp, int) or timestamp < 0:
        raise ValueError("Timestamp must be a non-negative integer")

def timestamp_to_human_readable(timestamp):
    validate_timestamp(timestamp)
    return datetime.fromtimestamp(timestamp).strftime('%d-%b-%Y %H:%M:%S')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_human_readable(sample_timestamp))