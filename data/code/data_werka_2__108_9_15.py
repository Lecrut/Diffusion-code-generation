from datetime import datetime
from typing import Union

DAY_OF_MONTH_MIN = 1
DAY_OF_MONTH_MAX = 31

def _validate_datetime_instance(dt: Union[datetime, object]) -> None:
    if not isinstance(dt, datetime):
        raise ValueError(f"Expected datetime instance, got {type(dt).__name__}")

def _extract_day_component(dt: datetime) -> int:
    day = dt.day
    if day < DAY_OF_MONTH_MIN or day > DAY_OF_MONTH_MAX:
        raise ValueError(f"Day value {day} is out of valid range 1-31")
    return day

def get_day_of_month(dt: datetime) -> int:
    _validate_datetime_instance(dt)
    return _extract_day_component(dt)

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29, 8, 0, 0)
    day_value = get_day_of_month(sample_dt)
    print(day_value)