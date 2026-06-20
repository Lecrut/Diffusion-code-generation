import time

WEEKDAY_NAMES = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def timestamp_to_weekday(timestamp):
    return WEEKDAY_NAMES[time.localtime(timestamp).tm_wday]

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(f"Timestamp {sample_timestamp}: {timestamp_to_weekday(sample_timestamp)}")