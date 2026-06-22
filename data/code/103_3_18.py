from datetime import datetime, timedelta
class TimeCalculator:
    def __init__(self, reference=None):
        self.ref = reference if reference else datetime.now()
        self.start = self.ref.replace(hour=0, minute=0, second=0, microsecond=0)
    def get_elapsed(self):
        return int((self.ref - self.start).total_seconds())
if __name__ == '__main__':
    sample = datetime(2024, 1, 1, 10, 0, 0)
    calc = TimeCalculator(sample)
    print(calc.get_elapsed())