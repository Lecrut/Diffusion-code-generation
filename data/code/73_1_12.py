from datetime import datetime, timedelta
from typing import Union

def calculate_time_diff(start_iso: str, end_iso: str) -> timedelta:
    _MICROSECOND_PRECISION = "%Y-%m-%dT%H:%M:%S.%f"
    _SECOND_PRECISION = "%Y-%m-%dT%H:%M:%S"
    
    parse_format: str = _MICROSECOND_PRECISION if "." in start_iso or "." in end_iso else _SECOND_PRECISION
    
    start_dt: datetime = datetime.strptime(start_iso, parse_format)
    end_dt: datetime = datetime.strptime(end_iso, parse_format)
    
    return end_dt - start_dt

if __name__ == '__main__':
    sample_start: str = "2024-02-29T08:15:00"
    sample_end: str = "2024-03-01T17:45:30"
    time_delta: timedelta = calculate_time_diff(sample_start, sample_end)
    print(time_delta)