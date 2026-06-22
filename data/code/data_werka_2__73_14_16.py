import datetime

class TimeDifferenceCalculator:
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        self.start = start
        self.end = end

    def get_total_seconds(self) -> int:
        delta = self.end - self.start
        return int(delta.total_seconds())

    def get_hours(self) -> int:
        total_seconds = self.get_total_seconds()
        return total_seconds // 3600

    def get_minutes(self) -> int:
        total_seconds = self.get_total_seconds()
        return (total_seconds // 60) % 60

    def get_seconds(self) -> int:
        total_seconds = self.get_total_seconds()
        return total_seconds % 60

    def get_formatted_difference(self) -> str:
        hours = self.get_hours()
        minutes = self.get_minutes()
        seconds = self.get_seconds()
        return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    start_dt = datetime.datetime(2023, 10, 1, 10, 30, 0)
    end_dt = datetime.datetime(2023, 10, 1, 14, 45, 30)
    calculator = TimeDifferenceCalculator(start_dt, end_dt)
    print(calculator.get_hours())
    print(calculator.get_minutes())
    print(calculator.get_seconds())
    print(calculator.get_formatted_difference())