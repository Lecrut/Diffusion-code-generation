from datetime import datetime
from typing import TypeVar

DT = TypeVar('DT')

def _validate_datetime_instance(dt: object) -> datetime:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime instance")
    return dt

def extract_day(dt: datetime) -> int:
    validated_dt = _validate_datetime_instance(dt)
    return validated_dt.day

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 0, 0, 0)
    day_value = extract_day(sample_dt)
    print(day_value)