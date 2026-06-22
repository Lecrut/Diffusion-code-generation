from datetime import datetime, timedelta

TIME_UNITS = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800,
}

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    return end - start

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    negative = total_seconds < 0
    abs_seconds = abs(total_seconds)
    weeks, remainder = divmod(abs_seconds, TIME_UNITS['weeks'])
    days, remainder = divmod(remainder, TIME_UNITS['days'])
    hours, remainder = divmod(remainder, TIME_UNITS['hours'])
    minutes, seconds = divmod(remainder, TIME_UNITS['minutes'])
    prefix = "-" if negative else ""
    return f"{prefix}{weeks}w {days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    start_time = datetime(2023, 11, 15, 8, 30, 0)
    end_time = datetime(2023, 11, 20, 14, 45, 30)
    diff = calculate_time_difference(start_time, end_time)
    formatted = format_timedelta(diff)
    print(formatted)
    print(diff)