from datetime import datetime, timedelta

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    return end - start

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    is_negative = total_seconds < 0
    abs_seconds = abs(total_seconds)
    
    days = abs_seconds // SECONDS_PER_DAY
    remainder = abs_seconds % SECONDS_PER_DAY
    
    hours = remainder // SECONDS_PER_HOUR
    remainder = remainder % SECONDS_PER_HOUR
    
    minutes = remainder // SECONDS_PER_MINUTE
    seconds = remainder % SECONDS_PER_MINUTE
    
    sign = "-" if is_negative else ""
    return f"{sign}{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    start_dt = datetime(2023, 11, 15, 8, 30, 0)
    end_dt = datetime(2023, 11, 18, 14, 45, 30)
    diff = calculate_time_difference(start_dt, end_dt)
    print(format_timedelta(diff))