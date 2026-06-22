from datetime import datetime, timedelta

class TimeDeltaCalculator:
    def __init__(self, start: datetime, end: datetime):
        if start > end:
            raise ValueError("Start time must be before or equal to end time")
        self.start = start
        self.end = end

    def get_hours(self) -> float:
        delta: timedelta = self.end - self.start
        total_seconds: float = delta.total_seconds()
        return total_seconds / 3600.0

if __name__ == '__main__':
    start_dt = datetime(2024, 5, 10, 9, 15, 0)
    end_dt = datetime(2024, 5, 10, 11, 45, 0)
    calculator = TimeDeltaCalculator(start_dt, end_dt)
    hours = calculator.get_hours()
    print(hours)