from datetime import datetime

class TimeCalculator:
    def time_elapsed(self, start_time, end_time):
        return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 1, 1, 12, 0, 0)
    end = datetime(2023, 1, 1, 14, 30, 0)
    print(calculator.time_elapsed(start, end))