from datetime import datetime

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')

if __name__ == '__main__':
    SAMPLE_TIMESTAMP = 1633072800
    formatted_date = timestamp_to_date(SAMPLE_TIMESTAMP)
    print(formatted_date)