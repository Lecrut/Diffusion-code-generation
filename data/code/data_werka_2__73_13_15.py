from datetime import datetime, timedelta

def compute_timedelta_hours(start: datetime, end: datetime) -> float:
    delta = end - start
    total_seconds = delta.total_seconds()
    return total_seconds / 3600

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime(2023, 1, 1, 14, 30, 0)
    result = compute_timedelta_hours(start_time, end_time)
    print(result)