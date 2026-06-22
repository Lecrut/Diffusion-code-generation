from datetime import datetime, timedelta

class DurationAnalyzer:
    def __init__(self, reference_time: datetime):
        self.reference_time = reference_time

    def calculate_delta(self, target_time: datetime) -> timedelta:
        return target_time - self.reference_time

    def get_hours(self, target_time: datetime) -> float:
        delta = self.calculate_delta(target_time)
        return delta.total_seconds() / 3600.0

    def get_minutes(self, target_time: datetime) -> float:
        delta = self.calculate_delta(target_time)
        return delta.total_seconds() / 60.0

if __name__ == '__main__':
    base_time = datetime(2024, 1, 1, 0, 0, 0)
    target = datetime(2024, 1, 1, 12, 30, 0)
    analyzer = DurationAnalyzer(base_time)
    hours_result = analyzer.get_hours(target)
    minutes_result = analyzer.get_minutes(target)
    print(hours_result)
    print(minutes_result)