import time

class DayOfWeekConverter:
    @staticmethod
    def get_day_of_week(timestamp):
        return time.strftime('%A', time.localtime(timestamp))

if __name__ == '__main__':
    sample_timestamp = 1678886400
    result = DayOfWeekConverter.get_day_of_week(sample_timestamp)
    print(f"Timestamp {sample_timestamp}: {result}")