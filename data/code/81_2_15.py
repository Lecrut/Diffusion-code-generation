from datetime import datetime

class TimeCalculator:
    def calculate_time_elapsed(self, start_time, end_time):
        return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 10, 1, 12, 0)
    end = datetime(2023, 10, 1, 14, 30)
    print(calculator.calculate_time_elapsed(start, end))