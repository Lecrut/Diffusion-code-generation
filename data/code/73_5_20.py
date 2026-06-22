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
    start_time = datetime(2023, 5, 15, 14, 30, 0)
    end_time = datetime(2023, 5, 15, 10, 15, 0)
    
    calculator = TimeDeltaCalculator(start_time, end_time)
    
    diff = calculator.get_difference()
    total_secs = calculator.get_total_seconds()
    abs_secs = calculator.get_absolute_seconds()
    
    print(diff)
    print(total_secs)
    print(abs_secs)