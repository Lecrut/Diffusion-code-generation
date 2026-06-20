from datetime import datetime

class TimeDurationCalculator:
    def calculate_elapsed_hours(self, start_time: str, end_time: str) -> float:
        time_format = "%Y-%m-%d %H:%M:%S"
        start_dt = datetime.strptime(start_time, time_format)
        end_dt = datetime.strptime(end_time, time_format)
        time_difference = end_dt - start_dt
        return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    calculator = TimeDurationCalculator()
    start = "2023-10-01 09:00:00"
    end = "2023-10-01 17:30:00"
    result = calculator.calculate_elapsed_hours(start, end)
    print(result)