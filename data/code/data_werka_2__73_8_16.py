from datetime import datetime, timedelta

class TimeCalculator:
    MINUTE_SECONDS = 60
    HOUR_SECONDS = 3600
    DAY_SECONDS = 86400

    @staticmethod
    def _validate_datetimes(start: datetime, end: datetime) -> None:
        if not isinstance(start, datetime):
            raise ValueError("Start argument must be a datetime object")
        if not isinstance(end, datetime):
            raise ValueError("End argument must be a datetime object")

    @staticmethod
    def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
        TimeCalculator._validate_datetimes(start, end)
        return end - start

if __name__ == '__main__':
    start_dt = datetime(2024, 5, 15, 8, 30, 0)
    end_dt = datetime(2024, 5, 15, 14, 45, 30)
    diff = TimeCalculator.calculate_time_difference(start_dt, end_dt)
    print(diff)