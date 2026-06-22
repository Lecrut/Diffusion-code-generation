from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if type(start) is not datetime:
        raise ValueError("start must be a datetime object")
    if type(end) is not datetime:
        raise ValueError("end must be a datetime object")
    return end - start

if __name__ == '__main__':
    start_dt = datetime(2023, 10, 1, 10, 0, 0)
    end_dt = datetime(2023, 10, 1, 12, 30, 45)
    result = calculate_time_difference(start_dt, end_dt)
    print(result)