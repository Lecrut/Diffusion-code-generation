from datetime import datetime, timedelta
class TimeCalculator:
    def __init__(self):
        self.now = datetime.now()
    def get_elapsed(self):
        start = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.now - start
        return int(delta.total_seconds())
if __name__ == '__main__':
    calc = TimeCalculator()
    print(calc.get_elapsed())