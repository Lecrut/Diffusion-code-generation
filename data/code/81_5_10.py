from datetime import datetime

def validate_timestamps(start_time, end_time):
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Both start_time and end_time must be instances of datetime")
    if start_time > end_time:
        raise ValueError("start_time must be before end_time")

def calculate_duration_in_hours(start_time, end_time):
    validate_timestamps(start_time, end_time)
    time_difference = end_time - start_time
    duration_hours = time_difference.total_seconds() / 3600
    return duration_hours

if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 0)
    result = calculate_duration_in_hours(time1, time2)
    print(result)