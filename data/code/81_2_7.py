from datetime import datetime

class TimeCalculator:
    SECONDS_PER_HOUR = 3600

    def calculate_elapsed_hours(self, start_time, end_time):
        time_difference = end_time - start_time
        return time_difference.total_seconds() / self.SECONDS_PER_HOUR

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 3, 14, 30)
    elapsed = calculator.calculate_elapsed_hours(start, end)
    print(elapsed)