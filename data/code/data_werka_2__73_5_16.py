from datetime import datetime, timedelta

class TimeDeltaCalculator:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def get_difference(self) -> timedelta:
        return self.end - self.start

    def get_total_seconds(self) -> float:
        return self.get_difference().total_seconds()

    def get_absolute_seconds(self) -> float:
        return abs(self.get_total_seconds())

if __name__ == '__main__':
    start_dt = datetime(2023, 5, 15, 14, 30, 0)
    end_dt = datetime(2023, 5, 15, 10, 15, 0)
    calculator = TimeDeltaCalculator(start_dt, end_dt)
    print(calculator.get_difference())
    print(calculator.get_total_seconds())
    print(calculator.get_absolute_seconds())