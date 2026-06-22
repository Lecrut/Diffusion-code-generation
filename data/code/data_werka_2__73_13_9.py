from datetime import datetime, timedelta
from typing import Union

class DurationConverter:
    SECONDS_IN_HOUR = 3600
    MINUTES_IN_HOUR = 60
    MILLISECONDS_IN_SECOND = 1000

    @staticmethod
    def _validate_inputs(start: datetime, end: datetime) -> None:
        if not isinstance(start, datetime):
            raise TypeError("Start must be a datetime object")
        if not isinstance(end, datetime):
            raise TypeError("End must be a datetime object")
        if start > end:
            raise ValueError("Start time cannot be after end time")

    @classmethod
    def get_hours_between(cls, start: datetime, end: datetime) -> float:
        cls._validate_inputs(start, end)
        delta: timedelta = end - start
        total_seconds: float = delta.total_seconds()
        return total_seconds / cls.SECONDS_IN_HOUR

if __name__ == '__main__':
    start_dt = datetime(2024, 3, 15, 6, 0, 0)
    end_dt = datetime(2024, 3, 15, 18, 45, 30)
    hours_elapsed = DurationConverter.get_hours_between(start_dt, end_dt)
    print(hours_elapsed)