from datetime import datetime

class TimestampConverter:
    def convert_timestamp(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%d-%b-%Y %H:%M:%S')

if __name__ == '__main__':
    converter = TimestampConverter()
    sample_timestamps = [1633072800, 1672531200]
    for timestamp in sample_timestamps:
        print(converter.convert_timestamp(timestamp))