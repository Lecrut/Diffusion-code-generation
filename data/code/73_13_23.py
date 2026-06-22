from datetime import datetime, timedelta

class DurationAnalyzer:
    def __init__(self, start_dt: datetime, end_dt: datetime):
        if end_dt < start_dt:
            raise ValueError("End time must be after start time")
        self.start_dt = start_dt
        self.end_dt = end_dt
        self._delta = end_dt - start_dt
        self._total_seconds = self._delta.total_seconds()

    def get_hours(self) -> float:
        return self._total_seconds / 3600.0

    def get_days(self) -> float:
        return self._total_seconds / 86400.0

    def get_total_seconds(self) -> float:
        return self._total_seconds

    def get_timedelta_object(self) -> timedelta:
        return self._delta

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 0, 0, 0)
    end_time = datetime(2023, 10, 1, 12, 30, 0)
    analyzer = DurationAnalyzer(start_time, end_time)
    print(analyzer.get_hours())
    print(analyzer.get_days())
    print(analyzer.get_total_seconds())
    print(analyzer.get_timedelta_object())