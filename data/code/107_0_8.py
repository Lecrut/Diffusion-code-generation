from datetime import datetime
import calendar

def format_datetime_iso(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("dt must be a datetime object")
    if not (1 <= dt.month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= dt.day <= 31):
        raise ValueError("Invalid day")
    if not (0 <= dt.hour <= 23):
        raise ValueError("Invalid hour")
    if not (0 <= dt.minute <= 59):
        raise ValueError("Invalid minute")
    if not (0 <= dt.second <= 59):
        raise ValueError("Invalid second")
    
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    
    max_day = calendar.monthrange(year, month)[1]
    if day > max_day:
        raise ValueError("Day out of range for month")
        
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime_iso(sample_dt)
    print(result)