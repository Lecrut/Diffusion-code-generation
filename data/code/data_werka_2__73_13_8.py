from datetime import datetime, timedelta

def compute_timedelta_hours(start: datetime, end: datetime) -> float:
    delta: timedelta = end - start
    total_seconds: float = delta.total_seconds()
    hours: float = total_seconds / 3600.0
    return hours

if __name__ == '__main__':
    start_time: datetime = datetime(2023, 1, 1, 10, 0, 0)
    end_time: datetime = datetime(2023, 1, 1, 14, 30, 0)
    result: float = compute_timedelta_hours(start_time, end_time)
    print(result)