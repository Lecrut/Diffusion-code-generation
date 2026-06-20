import datetime

def calculate_duration_hours(start_time: datetime.datetime, end_time: datetime.datetime) -> float:
    time_difference = end_time - start_time
    duration_seconds = time_difference.total_seconds()
    duration_hours = duration_seconds / 3600.0
    return duration_hours

if __name__ == '__main__':
    sample_start_time = datetime.datetime(2023, 10, 1, 9, 0, 0)
    sample_end_time = datetime.datetime(2023, 10, 1, 17, 30, 0)
    result = calculate_duration_hours(sample_start_time, sample_end_time)
    print(result)