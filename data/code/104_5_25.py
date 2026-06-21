from datetime import datetime
from typing import Union

def _validate_datetime_instance(value: Union[datetime, object]) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("Expected a datetime instance")
    return value

def compare_datetimes(first_dt: datetime, second_dt: datetime) -> str:
    validated_first = _validate_datetime_instance(first_dt)
    validated_second = _validate_datetime_instance(second_dt)
    
    if validated_first < validated_second:
        return "First is earlier"
    if validated_first > validated_second:
        return "Second is earlier"
    return "They are equal"

if __name__ == '__main__':
    dt_one = datetime(2024, 5, 10, 8, 30, 0)
    dt_two = datetime(2024, 5, 10, 8, 30, 0)
    outcome = compare_datetimes(dt_one, dt_two)
    print(outcome)