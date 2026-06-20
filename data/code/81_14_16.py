from datetime import datetime

def calculate_duration_hours(start_time: datetime, end_time: datetime) -> float:
    time_difference = end_time - start_time
    total_seconds = time_difference.total_seconds()
    hours = total_seconds / 3600.0
    return hours

if __name__ == '__main__':
    sample_start = datetime(2023, 1, 5, 8, 45, 0)
    sample_end = datetime(2023, 1, 7, 17, 15, 0)
    duration = calculate_duration_hours(sample_start, sample_end)
    print(f"Duration in hours: {duration}")