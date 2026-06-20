from datetime import datetime

class TimestampParser:
    DATE_FORMAT = '%Y/%m/%d'
    
    @staticmethod
    def timestamp_to_date(timestamp):
        return datetime.fromtimestamp(timestamp).strftime(TimestampParser.DATE_FORMAT)

if __name__ == '__main__':
    sample_timestamp = 1633072800
    formatted_date = TimestampParser.timestamp_to_date(sample_timestamp)
    print(formatted_date)