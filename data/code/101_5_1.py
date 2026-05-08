import datetime
def find_day_of_week_from_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%A')
if __name__ == '__main__':
    sample_timestamp_1 = 1678886400
    sample_timestamp_2 = 1609459200
    print(f"Timestamp {sample_timestamp_1}: {find_day_of_week_from_timestamp(sample_timestamp_1)}")
    print(f"Timestamp {sample_timestamp_2}: {find_day_of_week_from_timestamp(sample_timestamp_2)}")