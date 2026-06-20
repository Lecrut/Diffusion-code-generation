from datetime import datetime

class TimeCalculator:
    def calculate_elapsed_hours(self, start_time, end_time):
        return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 10, 1, 12, 0)
    end = datetime(2023, 10, 1, 14, 30)
    print(calculator.calculate_elapsed_hours(start, end))