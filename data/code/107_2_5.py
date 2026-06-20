from datetime import datetime

DATE_FORMAT = '%Y/%m/%d'

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime(DATE_FORMAT)

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatted_date = timestamp_to_date(sample_timestamp)
    print(formatted_date)