from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def _validate_datetimes(start: datetime, end: datetime) -> None:
        if not isinstance(start, datetime):
            raise ValueError("Start argument must be a datetime object")
        if not isinstance(end, datetime):
            raise ValueError("End argument must be a datetime object")

    @classmethod
    def calculate_time_difference(cls, start: datetime, end: datetime) -> timedelta:
        cls._validate_datetimes(start, end)
        return end - start

if __name__ == '__main__':
    start_time = datetime(2024, 6, 15, 8, 30, 0)
    end_time = datetime(2024, 6, 15, 14, 45, 30)
    diff = TimeCalculator.calculate_time_difference(start_time, end_time)
    print(diff)