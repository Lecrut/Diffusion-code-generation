from datetime import datetime, timedelta

class TimeDiffer:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def get_difference(self) -> timedelta:
        return self.end - self.start

    def get_absolute_difference(self) -> timedelta:
        diff = self.get_difference()
        if diff.total_seconds() < 0:
            return -diff
        return diff

    def get_seconds(self) -> float:
        return self.get_difference().total_seconds()

if __name__ == '__main__':
    start_time = datetime(2023, 12, 25, 8, 30, 0)
    end_time = datetime(2023, 12, 25, 10, 45, 0)
    differ = TimeDiffer(start_time, end_time)
    diff = differ.get_difference()
    abs_diff = differ.get_absolute_difference()
    secs = differ.get_seconds()
    print(diff)
    print(abs_diff)
    print(secs)