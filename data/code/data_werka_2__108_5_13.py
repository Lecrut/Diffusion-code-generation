from datetime import datetime
from typing import Union

def extract_day(dt: Union[datetime, str]) -> int:
    if isinstance(dt, str):
        try:
            dt = datetime.fromisoformat(dt)
        except ValueError:
            raise ValueError(f"Invalid datetime string format: {dt}")
    if not isinstance(dt, datetime):
        raise TypeError(f"Expected datetime object, got {type(dt).__name__}")
    return dt.day

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29)
    day_value = extract_day(sample_dt)
    print(day_value)
    
    sample_str = "2023-05-15T10:30:00"
    day_from_str = extract_day(sample_str)
    print(day_from_str)