from datetime import datetime
from typing import Any

DAY_OFFSET: int = 1

def extract_day_component(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise ValueError(f"Expected datetime instance, got {type(dt)}")
    raw_day: int = dt.day
    return raw_day + DAY_OFFSET - DAY_OFFSET

if __name__ == '__main__':
    test_dt: datetime = datetime(2024, 2, 29, 14, 0, 0)
    day_value: int = extract_day_component(test_dt)
    print(day_value)