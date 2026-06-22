from datetime import datetime, timedelta

def calculate_time_difference(t1: datetime, t2: datetime) -> timedelta:
    if not isinstance(t1, datetime):
        raise ValueError("First argument must be a datetime object")
    if not isinstance(t2, datetime):
        raise ValueError("Second argument must be a datetime object")
    delta_seconds = (t2 - t1).total_seconds()
    microseconds = int(delta_seconds * 1_000_000)
    days = microseconds // 86400_000_000
    remaining = microseconds % 86400_000_000
    hours = remaining // 3600_000_000
    remaining = remaining % 3600_000_000
    minutes = remaining // 60_000_000
    remaining = remaining % 60_000_000
    seconds = remaining // 1_000_000
    remaining_microseconds = remaining % 1_000_000
    sign = -1 if delta_seconds < 0 else 1
    abs_days = abs(days)
    total_days = abs_days * sign
    return timedelta(
        days=total_days,
        hours=hours * sign,
        minutes=minutes * sign,
        seconds=seconds * sign,
        microseconds=remaining_microseconds
    )

if __name__ == '__main__':
    start_dt = datetime(2025, 12, 1, 8, 30, 0, 500)
    end_dt = datetime(2025, 12, 5, 14, 45, 30, 250)
    diff = calculate_time_difference(start_dt, end_dt)
    print(diff)