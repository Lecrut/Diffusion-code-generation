from datetime import datetime

def timestamp_to_date(timestamp):
    try:
        return datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')
    except (TypeError, OSError) as e:
        raise ValueError("Invalid timestamp") from e

if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_date(sample_timestamp))