import time

EPOCH_TIMESTAMP = 0

def find_day_of_week_from_timestamp(timestamp):
    return time.strftime('%A', time.localtime(timestamp - EPOCH_TIMESTAMP))

if __name__ == '__main__':
    sample_timestamp_1 = 1678886400
    result_1 = find_day_of_week_from_timestamp(sample_timestamp_1)
    print(f"Timestamp: {sample_timestamp_1}, Day of Week: {result_1}")