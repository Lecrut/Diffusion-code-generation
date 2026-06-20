import datetime

class TimestampConverter:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def timestamp_to_iso(unix_timestamp):
        dt_object = datetime.datetime.utcfromtimestamp(unix_timestamp)
        return dt_object.strftime(TimestampConverter.DATE_FORMAT) + 'Z'

if __name__ == '__main__':
    converter = TimestampConverter()
    sample_timestamp1 = 1633072800
    print(converter.timestamp_to_iso(sample_timestamp1))