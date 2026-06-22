from datetime import datetime, timedelta

class TimeElapsedCalculator:
    def __init__(self, reference_time=None):
        self.reference_time = reference_time if reference_time else datetime.now()
        self.day_start = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    def get_seconds(self):
        delta = self.reference_time - self.day_start
        return int(delta.total_seconds())

if __name__ == '__main__':
    sample_time = datetime(2024, 11, 1, 9, 15, 30)
    calculator = TimeElapsedCalculator(sample_time)
    print(calculator.get_seconds())