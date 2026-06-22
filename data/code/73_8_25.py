from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    return end - start

if __name__ == '__main__':
    start_time = datetime(2023, 5, 15, 8, 30, 0)
    end_time = datetime(2023, 5, 15, 14, 45, 30)
    diff = calculate_time_difference(start_time, end_time)
    print(diff)