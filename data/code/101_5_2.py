import datetime
def find_day_of_week_from_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%A')
if __name__ == '__main__':
    sample_timestamp_1 = 1678886400
    result_1 = find_day_of_week_from_timestamp(sample_timestamp_1)
    print(f"Timestamp: {sample_timestamp_1}, Day of Week: {result_1}")
    sample_timestamp_2 = 1609459200
    result_2 = find_day_of_week_from_timestamp(sample_timestamp_2)
    print(f"Timestamp: {sample_timestamp_2}, Day of Week: {result_2}")
    sample_timestamp_3 = 1577836800
    result_3 = find_day_of_week_from_timestamp(sample_timestamp_3)
    print(f"Timestamp: {sample_timestamp_3}, Day of Week: {result_3}")