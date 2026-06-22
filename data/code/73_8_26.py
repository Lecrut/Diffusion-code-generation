from datetime import datetime, timedelta

def _validate_datetime(value, name):
    if not isinstance(value, datetime):
        raise ValueError(f"{name} must be a datetime object, got {type(value).__name__}")
    return value

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    _validate_datetime(start, "start")
    _validate_datetime(end, "end")
    return end - start

if __name__ == '__main__':
    start_time = datetime(2024, 5, 15, 8, 30, 0)
    end_time = datetime(2024, 5, 15, 14, 45, 30)
    difference = calculate_time_difference(start_time, end_time)
    print(difference)