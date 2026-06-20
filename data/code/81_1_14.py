from datetime import datetime

def calculate_elapsed_hours(start_time: datetime, end_time: datetime) -> float:
    time_difference = end_time - start_time
    elapsed_hours = time_difference.total_seconds() / 3600.0
    return elapsed_hours

if __name__ == '__main__':
    sample_start_time = datetime(2023, 4, 15, 9, 0)
    sample_end_time = datetime(2023, 4, 17, 16, 45)
    hours_difference = calculate_elapsed_hours(sample_start_time, sample_end_time)
    print(hours_difference)