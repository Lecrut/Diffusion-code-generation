import time

class DateConverter:
    @staticmethod
    def timestamp_to_weekday(timestamp):
        return time.strftime('%A', time.localtime(timestamp))

if __name__ == '__main__':
    converter = DateConverter()
    sample_timestamp_1 = 1678886400
    print(f"Timestamp {sample_timestamp_1}: {converter.timestamp_to_weekday(sample_timestamp_1)}")