from datetime import datetime

def format_datetime_iso(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2024, 1, 15, 9, 5, 30)
    result = format_datetime_iso(sample_dt)
    print(result)