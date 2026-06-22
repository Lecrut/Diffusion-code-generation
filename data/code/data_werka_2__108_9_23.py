from datetime import datetime
from typing import TypeGuard

def is_valid_datetime_instance(obj: object) -> TypeGuard[datetime]:
    return isinstance(obj, datetime)

def get_day_of_month(dt: datetime) -> int:
    if not is_valid_datetime_instance(dt):
        raise ValueError("Input must be a datetime instance")
    return dt.day

if __name__ == '__main__':
    sample_datetime = datetime(2024, 2, 29, 8, 0, 0)
    day_value = get_day_of_month(sample_datetime)
    print(day_value)