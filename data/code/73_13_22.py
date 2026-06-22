from datetime import datetime

def calculate_duration_in_hours(start_time: datetime, end_time: datetime) -> float:
    if not isinstance(start_time, datetime):
        raise ValueError("start_time must be a datetime object")
    if not isinstance(end_time, datetime):
        raise ValueError("end_time must be a datetime object")
    if start_time >= end_time:
        raise ValueError("start_time must be strictly before end_time")
    seconds_elapsed = (end_time - start_time).total_seconds()
    return seconds_elapsed / 3600.0

if __name__ == '__main__':
    start = datetime(2024, 1, 1, 0, 0, 0)
    end = datetime(2024, 1, 1, 23, 59, 59)
    hours = calculate_duration_in_hours(start, end)
    print(hours)