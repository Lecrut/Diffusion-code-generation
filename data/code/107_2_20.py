from datetime import datetime

class DateFormatter:
    DATE_FORMAT = '%Y/%m/%d'
    
    def timestamp_to_date(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime(self.DATE_FORMAT)

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_timestamp = 1633072800
    formatted_date = formatter.timestamp_to_date(sample_timestamp)
    print(formatted_date)