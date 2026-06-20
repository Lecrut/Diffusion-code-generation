from datetime import datetime

class TimestampToDate:
    DATE_FORMAT = '%Y/%m/%d'
    
    @staticmethod
    def timestamp_to_date(timestamp):
        return datetime.fromtimestamp(timestamp).strftime(TimestampToDate.DATE_FORMAT)

if __name__ == '__main__':
    parser = TimestampToDate()
    sample_timestamp = 1633072800
    formatted_date = parser.timestamp_to_date(sample_timestamp)
    print(formatted_date)