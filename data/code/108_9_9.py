from datetime import datetime
from typing import Union

class DateExtractor:
    DAY_ATTRIBUTE = "day"

    @staticmethod
    def _validate_datetime(dt: datetime) -> datetime:
        if not isinstance(dt, datetime):
            raise ValueError("Input must be a datetime instance")
        return dt

    @classmethod
    def get_day_of_month(cls, dt: datetime) -> int:
        validated_dt = cls._validate_datetime(dt)
        return getattr(validated_dt, cls.DAY_ATTRIBUTE)

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 10, 0, 0)
    extractor = DateExtractor()
    day_value = extractor.get_day_of_month(sample_dt)
    print(day_value)