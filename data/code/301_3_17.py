from datetime import datetime
DATE_FORMAT = '%d-%b-%Y %H:%M:%S'

def timestamp_to_human_readable(timestamp):
    return datetime.fromtimestamp(timestamp).strftime(DATE_FORMAT)
if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(timestamp_to_human_readable(sample_timestamp))