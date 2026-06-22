from datetime import datetime

def _validate_datetime_input(dt) -> None:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")

def _format_component(value: int, width: int) -> str:
    return str(value).zfill(width)

def format_datetime_iso8601(dt: datetime) -> str:
    _validate_datetime_input(dt)
    
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
        
    month_str = _format_component(month, 2)
    day_str = _format_component(day, 2)
    hour_str = _format_component(hour, 2)
    minute_str = _format_component(minute, 2)
    second_str = _format_component(second, 2)
    
    return f"{year}-{month_str}-{day_str} {hour_str}:{minute_str}:{second_str}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime_iso8601(sample_dt)
    print(result)