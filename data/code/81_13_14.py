from datetime import datetime

class TimeDurationCalculator:
    @staticmethod
    def calculate_duration(start_time: str, end_time: str) -> float:
        start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        duration = end - start
        return duration.total_seconds() / 3600

if __name__ == '__main__':
    sample_start = "2023-10-01 12:00:00"
    sample_end = "2023-10-01 14:30:00"
    calculator = TimeDurationCalculator()
    duration_in_hours = calculator.calculate_duration(sample_start, sample_end)
    print(duration_in_hours)