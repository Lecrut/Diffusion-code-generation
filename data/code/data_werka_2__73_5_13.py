from datetime import datetime, timedelta

def compute_time_delta(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    return end - start

if __name__ == '__main__':
    start_time = datetime(2023, 5, 15, 8, 30, 0)
    end_time = datetime(2023, 5, 15, 6, 15, 0)
    delta = compute_time_delta(start_time, end_time)
    print(delta)