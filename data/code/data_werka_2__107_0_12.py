from datetime import datetime

def format_datetime_to_iso(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime instance")
    
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    if not (0 <= hour <= 23):
        raise ValueError("Hour out of range")
    if not (0 <= minute <= 59):
        raise ValueError("Minute out of range")
    if not (0 <= second <= 59):
        raise ValueError("Second out of range")
    
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_time = datetime(2024, 1, 15, 9, 5, 30)
    formatted_str = format_datetime_to_iso(sample_time)
    print(formatted_str)