from datetime import datetime
from enum import IntEnum

class DayCategory(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def is_weekday(timestamp: str) -> bool:
    parsed_dt = datetime.fromisoformat(timestamp)
    day_index = parsed_dt.weekday()
    is_week = day_index < 5
    return bool(is_week)

if __name__ == '__main__':
    sample_timestamp = '2023-10-07T12:00:00'
    parsed_dt = datetime.fromisoformat(sample_timestamp)
    day_name = DAY_NAMES.get(parsed_dt.weekday(), "Unknown")
    result = is_weekday(sample_timestamp)
    print(f"{sample_timestamp} is {day_name}: {result}")