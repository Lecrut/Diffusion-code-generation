from datetime import datetime

def calculate_duration_in_hours(start_time, end_time):
    time_difference = end_time - start_time
    duration_hours = time_difference.total_seconds() / 3600
    return duration_hours

if __name__ == '__main__':
    sample_start = datetime(2023, 1, 5, 9, 0, 0)
    sample_end = datetime(2023, 1, 8, 17, 45, 0)
    duration = calculate_duration_in_hours(sample_start, sample_end)
    print(duration)