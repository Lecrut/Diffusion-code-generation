from datetime import datetime, timedelta
class SecondsCalculator:
    def __init__(self, target_time=None):
        self.target_time = target_time if target_time is not None else datetime.now()
        self.day_start = self.target_time.replace(hour=0, minute=0, second=0, microsecond=0)
    def get_elapsed_seconds(self):
        delta = self.target_time - self.day_start
        return int(delta.total_seconds())
if __name__ == '__main__':
    sample_time = datetime(2023, 11, 5, 9, 15, 30)
    calc = SecondsCalculator(sample_time)
    print(calc.get_elapsed_seconds())