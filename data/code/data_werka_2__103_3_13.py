from datetime import datetime, timedelta

class TimeElapsed:
    def __init__(self, reference: datetime = None):
        self.ref = reference if reference else datetime.now()
        self.start = self.ref.replace(hour=0, minute=0, second=0, microsecond=0)
    def total_seconds(self) -> int:
        delta = self.ref - self.start
        return int(delta.total_seconds())

if __name__ == '__main__':
    sample = datetime(2023, 11, 10, 8, 15, 30)
    calculator = TimeElapsed(sample)
    print(calculator.total_seconds())