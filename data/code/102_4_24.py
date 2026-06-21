from datetime import datetime
from enum import IntEnum

class DayCategory(IntEnum):
    WEEKDAY = 0
    WEEKEND = 1

class TimestampValidator:
    def __init__(self, timestamp_str: str):
        self._dt = datetime.fromisoformat(timestamp_str)

    def is_weekday(self) -> bool:
        return self._dt.weekday() < 5

    def get_day_category(self) -> DayCategory:
        if self.is_weekday():
            return DayCategory.WEEKDAY
        return DayCategory.WEEKEND

if __name__ == '__main__':
    validator = TimestampValidator("2023-10-07T12:00:00")
    print(validator.is_weekday())
    print(validator.get_day_category())