from datetime import datetime

class TimeCalculator:
    def calculate_elapsed_hours(self, start_time, end_time):
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Both start_time and end_time must be datetime objects.")
        if start_time > end_time:
            raise ValueError("start_time must be before end_time.")
        time_difference = end_time - start_time
        return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 3, 14, 30)
    elapsed = calculator.calculate_elapsed_hours(start, end)
    print(elapsed)