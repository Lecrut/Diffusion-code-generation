from datetime import datetime, timedelta

class TimeCalculator:
    def calculate_time_difference(self, start: datetime, end: datetime) -> timedelta:
        if not isinstance(start, datetime):
            raise ValueError("start must be a datetime object")
        if not isinstance(end, datetime):
            raise ValueError("end must be a datetime object")
        return end - start

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_dt = datetime(2023, 5, 15, 8, 30, 0)
    end_dt = datetime(2023, 5, 15, 14, 45, 30)
    result = calculator.calculate_time_difference(start_dt, end_dt)
    print(result)