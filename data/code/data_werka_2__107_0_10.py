from datetime import datetime

def validate_datetime(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.year < 1 or dt.year > 9999:
        raise ValueError("Year out of valid range")
    if dt.month < 1 or dt.month > 12:
        raise ValueError("Month out of valid range")
    if dt.day < 1 or dt.day > 31:
        raise ValueError("Day out of valid range")
    if dt.hour < 0 or dt.hour > 23:
        raise ValueError("Hour out of valid range")
    if dt.minute < 0 or dt.minute > 59:
        raise ValueError("Minute out of valid range")
    if dt.second < 0 or dt.second > 59:
        raise ValueError("Second out of valid range")
    return True

def format_datetime_to_iso(dt):
    validate_datetime(dt)
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 9, 5, 30)
    result = format_datetime_to_iso(sample_dt)
    print(result)