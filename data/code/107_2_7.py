from datetime import datetime

class TimestampFormatter:
    DATE_FORMAT = '%Y/%m/%d'
    
    @staticmethod
    def timestamp_to_date(timestamp):
        return datetime.fromtimestamp(timestamp).strftime(TimestampFormatter.DATE_FORMAT)

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatter = TimestampFormatter()
    formatted_date = formatter.timestamp_to_date(sample_timestamp)
    print(formatted_date)