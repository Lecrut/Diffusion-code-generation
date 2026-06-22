from datetime import datetime, timedelta

class TimeCalculator:
    def calculate_difference(self, start_time: datetime, end_time: datetime) -> timedelta:
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Both arguments must be datetime instances")
        return end_time - start_time

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2023, 10, 1, 8, 0, 0)
    t2 = datetime(2023, 10, 5, 17, 30, 45)
    delta = calculator.calculate_difference(t1, t2)
    print(delta)