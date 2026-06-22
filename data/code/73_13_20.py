from datetime import datetime

def get_duration_in_hours(start: datetime, end: datetime) -> float:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError("Inputs must be datetime objects")
    if start == end:
        return 0.0
    if start > end:
        raise ValueError("Start time must be before end time")
    seconds_diff = (end - start).total_seconds()
    return seconds_diff / 3600.0

if __name__ == '__main__':
    t1 = datetime(2024, 1, 1, 0, 0, 0)
    t2 = datetime(2024, 1, 1, 12, 30, 0)
    print(get_duration_in_hours(t1, t2))