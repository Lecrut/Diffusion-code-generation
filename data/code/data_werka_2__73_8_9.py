from datetime import datetime, timedelta
import sys

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if type(start) is not datetime or type(end) is not datetime:
        raise ValueError("Arguments must be datetime instances")
    return end - start

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    sign = "-" if td.days < 0 else ""
    return f"{sign}{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    start_dt = datetime(2023, 10, 1, 10, 0, 0)
    end_dt = datetime(2023, 10, 1, 12, 30, 45)
    diff = calculate_time_difference(start_dt, end_dt)
    print(format_timedelta(diff))
    print(diff)