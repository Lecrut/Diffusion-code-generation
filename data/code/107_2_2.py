from datetime import datetime

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')
if __name__ == '__main__':
    print(timestamp_to_date(1633072800))