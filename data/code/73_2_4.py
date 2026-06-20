from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, start_time: datetime, end_time: datetime) -> timedelta:
        return end_time - start_time

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 10, 1, 12, 0, 0)
    end = datetime(2023, 10, 1, 14, 30, 0)
    difference = calculator.calculate_difference(start, end)
    print(difference)