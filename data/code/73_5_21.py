from datetime import datetime, timedelta

def compute_time_span(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime instance")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime instance")
    return end - start

if __name__ == '__main__':
    t_start = datetime(2024, 5, 15, 8, 30, 0)
    t_end = datetime(2024, 5, 15, 10, 45, 0)
    span = compute_time_span(t_start, t_end)
    print(span)