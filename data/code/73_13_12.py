from datetime import datetime, timedelta

def calculate_hours_between(start: datetime, end: datetime) -> float:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise TypeError("Arguments must be datetime objects")
    if start == end:
        return 0.0
    if start > end:
        raise ValueError("Start time must be earlier than end time")
    duration: timedelta = end - start
    total_seconds: float = duration.total_seconds()
    hours: float = total_seconds / 3600.0
    return hours

if __name__ == '__main__':
    initial_dt: datetime = datetime(2024, 1, 1, 0, 0, 0)
    final_dt: datetime = datetime(2024, 1, 1, 12, 30, 45)
    elapsed_hours: float = calculate_hours_between(initial_dt, final_dt)
    print(elapsed_hours)