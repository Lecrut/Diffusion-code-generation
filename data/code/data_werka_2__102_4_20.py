from datetime import datetime
from enum import IntEnum

class DayCategory(IntEnum):
    WEEKDAY = 0
    WEEKEND = 1

class TimeValidator:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def parse_timestamp(ts: str) -> datetime:
        return datetime.fromisoformat(ts)

    @classmethod
    def is_weekday(cls, timestamp: str) -> bool:
        dt = cls.parse_timestamp(timestamp)
        return dt.weekday() < cls.WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_timestamp = '2023-10-07T12:00:00'
    result = TimeValidator.is_weekday(sample_timestamp)
    print(result)