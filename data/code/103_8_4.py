import datetime
def calculate_time_difference(timestamp):
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    difference = now - start_of_day
    return difference
if __name__ == '__main__':
    sample_timestamp = datetime.datetime(2023, 10, 27, 14, 35, 10)
    difference = calculate_time_difference(sample_timestamp)
    print(f"Sample Timestamp: {sample_timestamp}")
    print(f"Difference from start of day: {difference}")