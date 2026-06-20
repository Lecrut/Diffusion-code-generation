from datetime import datetime

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatted_date = timestamp_to_date(sample_timestamp)
    print(formatted_date)

    another_sample_timestamp = 1609459200
    another_formatted_date = timestamp_to_date(another_sample_timestamp)
    print(another_formatted_date)