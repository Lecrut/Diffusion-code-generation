from datetime import datetime

class TimestampConverter:
    DATE_FORMAT = '%d-%b-%Y %H:%M:%S'
    
    @staticmethod
    def convert_timestamp(timestamp):
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object.strftime(TimestampConverter.DATE_FORMAT)

if __name__ == '__main__':
    converter = TimestampConverter()
    sample_timestamps = [1633072800, 1672531200]
    for timestamp in sample_timestamps:
        print(converter.convert_timestamp(timestamp))