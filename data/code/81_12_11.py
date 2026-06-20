from datetime import datetime

class TimeCalculator:
    def elapsed_time_in_hours(self, start_time: datetime, end_time: datetime) -> float:
        time_difference = end_time - start_time
        return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 1, 1, 9, 0)
    end = datetime(2023, 1, 1, 17, 30)
    result = calculator.elapsed_time_in_hours(start, end)
    print(result)