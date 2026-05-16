from datetime import datetime
def calculate_elapsed_minutes(dt):
    midnight = datetime(dt.year, dt.month, dt.day, 0, 0)
    time_difference = dt - midnight
    total_minutes = time_difference.total_seconds() / 60
    return int(total_minutes)
if __name__ == '__main__':
    sample_datetime_1 = datetime(2023, 10, 27, 14, 30)
    result_1 = calculate_elapsed_minutes(sample_datetime_1)
    print(result_1)
    sample_datetime_2 = datetime(2024, 1, 1, 0, 0)
    result_2 = calculate_elapsed_minutes(sample_datetime_2)
    print(result_2)
    sample_datetime_3 = datetime(2023, 12, 31, 23, 59)
    result_3 = calculate_elapsed_minutes(sample_datetime_3)
    print(result_3)