from datetime import datetime

def validate_timestamp(timestamp):
    if not isinstance(timestamp, int) or timestamp < 0:
        raise ValueError("Invalid timestamp")

def timestamp_to_date(timestamp):
    validate_timestamp(timestamp)
    return datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatted_date = timestamp_to_date(sample_timestamp)
    print(formatted_date)