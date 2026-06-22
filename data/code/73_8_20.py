from datetime import datetime, timedelta

class TimeCalculator:
    MINUTE_SECONDS = 60
    HOUR_SECONDS = 3600
    DAY_SECONDS = 86400

    @staticmethod
    def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
        if type(start) is not datetime or type(end) is not datetime:
            raise ValueError("Arguments must be datetime instances")
        return end - start

if __name__ == '__main__':
    start_dt = datetime(2024, 5, 15, 8, 30, 0)
    end_dt = datetime(2024, 5, 16, 14, 45, 30)
    result = TimeCalculator.calculate_time_difference(start_dt, end_dt)
    print(result)