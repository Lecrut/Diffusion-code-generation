from datetime import datetime
from enum import IntEnum

class DayCategory(IntEnum):
    WEEKDAY = 0
    WEEKEND = 1

DAY_TYPE_MAP = {
    0: DayCategory.WEEKDAY,
    1: DayCategory.WEEKDAY,
    2: DayCategory.WEEKDAY,
    3: DayCategory.WEEKDAY,
    4: DayCategory.WEEKDAY,
    5: DayCategory.WEEKEND,
    6: DayCategory.WEEKEND,
}

def validate_timestamp_as_weekday(timestamp_str: str) -> bool:
    parsed_dt = datetime.fromisoformat(timestamp_str)
    day_index = parsed_dt.weekday()
    category = DAY_TYPE_MAP.get(day_index)
    if category is None:
        raise ValueError(f"Unsupported day index: {day_index}")
    return category == DayCategory.WEEKDAY

if __name__ == '__main__':
    test_ts = "2023-10-23T09:00:00"
    is_valid = validate_timestamp_as_weekday(test_ts)
    print(is_valid)