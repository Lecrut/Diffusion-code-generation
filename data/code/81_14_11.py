from datetime import datetime

def elapsed_time_in_hours(start_time: datetime, end_time: datetime) -> float:
    time_difference = end_time - start_time
    return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    sample_start_time = datetime(2023, 10, 1, 12, 0, 0)
    sample_end_time = datetime(2023, 10, 1, 14, 30, 0)
    print(elapsed_time_in_hours(sample_start_time, sample_end_time))