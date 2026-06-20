from datetime import datetime

class TimestampFormatter:
    DATE_FORMAT = '%Y/%m/%d'

    @classmethod
    def format_timestamp(cls, timestamp):
        return datetime.fromtimestamp(timestamp).strftime(cls.DATE_FORMAT)

if __name__ == '__main__':
    sample_timestamps = [1633072800, 1609459200, 1672531200]
    formatter = TimestampFormatter()
    
    for timestamp in sample_timestamps:
        print(formatter.format_timestamp(timestamp))