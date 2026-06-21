from datetime import datetime
from enum import IntEnum
from typing import Union

class DayCategory(IntEnum):
    WEEKDAY = 0
    WEEKEND = 1

class TimestampValidator:
    def __init__(self, raw_timestamp: Union[str, datetime]):
        if isinstance(raw_timestamp, str):
            self.dt = datetime.fromisoformat(raw_timestamp)
        elif isinstance(raw_timestamp, datetime):
            self.dt = raw_timestamp
        else:
            raise ValueError("Timestamp must be a string or datetime object")

    def is_weekday(self) -> bool:
        return self.dt.weekday() < 5

    def get_day_category(self) -> DayCategory:
        if self.is_weekday():
            return DayCategory.WEEKDAY
        return DayCategory.WEEKEND

    def format_day_name(self) -> str:
        return self.dt.strftime("%A")

if __name__ == '__main__':
    validator_instance = TimestampValidator("2023-10-07T12:00:00")
    print(validator_instance.is_weekday())
    print(validator_instance.get_day_category())
    print(validator_instance.format_day_name())

    weekend_validator = TimestampValidator("2023-10-08T12:00:00")
    print(weekend_validator.is_weekday())
    print(weekend_validator.get_day_category())
    print(weekend_validator.format_day_name())