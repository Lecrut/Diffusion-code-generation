from datetime import datetime, timedelta

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError("Arguments must be datetime instances")
    return end - start

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    sign = "-" if total_seconds < 0 else ""
    abs_seconds = abs(total_seconds)
    days, remainder = divmod(abs_seconds, SECONDS_PER_DAY)
    hours, remainder = divmod(remainder, SECONDS_PER_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_PER_MINUTE)
    return f"{sign}{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    start_dt = datetime(2023, 10, 1, 10, 0, 0)
    end_dt = datetime(2023, 10, 1, 12, 30, 45)
    diff = calculate_time_difference(start_dt, end_dt)
    print(format_timedelta(diff))