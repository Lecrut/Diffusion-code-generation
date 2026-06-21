from datetime import datetime

def _validate_datetime_component(value, min_val, max_val, name):
    if not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    if value < min_val or value > max_val:
        raise ValueError(f"{name} out of range [{min_val}, {max_val}]")

def _format_component(value, width=2):
    return f"{value:0{width}d}"

def format_datetime_to_iso8601(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    _validate_datetime_component(dt.year, 1, 9999, "year")
    _validate_datetime_component(dt.month, 1, 12, "month")
    _validate_datetime_component(dt.day, 1, 31, "day")
    _validate_datetime_component(dt.hour, 0, 23, "hour")
    _validate_datetime_component(dt.minute, 0, 59, "minute")
    _validate_datetime_component(dt.second, 0, 59, "second")
    
    year_str = _format_component(dt.year, 4)
    month_str = _format_component(dt.month)
    day_str = _format_component(dt.day)
    hour_str = _format_component(dt.hour)
    minute_str = _format_component(dt.minute)
    second_str = _format_component(dt.second)
    
    return f"{year_str}-{month_str}-{day_str} {hour_str}:{minute_str}:{second_str}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime_to_iso8601(sample_dt)
    print(result)