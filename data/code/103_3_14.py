from datetime import datetime, timedelta
class TodaySeconds:
    def __init__(self, ref=None):
        self.ref = ref if ref else datetime.now()
        self.day_start = self.ref.replace(hour=0, minute=0, second=0, microsecond=0)
    def count(self):
        return int((self.ref - self.day_start).total_seconds())
if __name__ == '__main__':
    sample = datetime(2025, 1, 1, 12, 0, 0)
    t = TodaySeconds(sample)
    print(t.count())