from datetime import datetime, timedelta

def get_hours_between(dt1: datetime, dt2: datetime) -> float:
    if dt1 == dt2:
        return 0.0
    if dt1 > dt2:
        dt1, dt2 = dt2, dt1
    diff: timedelta = dt2 - dt1
    return diff.total_seconds() / 3600.0

if __name__ == '__main__':
    time_a: datetime = datetime(2024, 11, 1, 12, 0, 0)
    time_b: datetime = datetime(2024, 11, 1, 18, 20, 0)
    output: float = get_hours_between(time_a, time_b)
    print(output)