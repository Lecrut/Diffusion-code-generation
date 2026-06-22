from datetime import datetime, timedelta

def get_absolute_time_span(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError("Inputs must be datetime instances")
    diff = end - start
    if diff.total_seconds() < 0:
        return -diff
    return diff

if __name__ == '__main__':
    t1 = datetime(2024, 5, 15, 14, 30, 0)
    t2 = datetime(2024, 5, 15, 12, 0, 0)
    span = get_absolute_time_span(t1, t2)
    print(span)