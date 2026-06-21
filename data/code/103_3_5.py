from datetime import datetime, timedelta

class DayTimer:
    def __init__(self, reference=None):
        self.ref = reference if reference else datetime.now()
        self.day_start = self.ref.replace(hour=0, minute=0, second=0, microsecond=0)
    def elapsed_seconds(self):
        delta = self.ref - self.day_start
        return int(delta.total_seconds())

if __name__ == '__main__':
    sample = datetime(2024, 5, 20, 10, 30, 15)
    timer = DayTimer(sample)
    print(timer.elapsed_seconds())