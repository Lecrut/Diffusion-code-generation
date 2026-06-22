from datetime import datetime, timedelta
class TodayElapsed:
    def __init__(self, current=None):
        self.now = current if current else datetime.now()
        self.start = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
    def seconds(self):
        delta = self.now - self.start
        return int(delta.total_seconds())
if __name__ == '__main__':
    ref = datetime(2025, 1, 1, 0, 1, 30)
    calc = TodayElapsed(ref)
    print(calc.seconds())