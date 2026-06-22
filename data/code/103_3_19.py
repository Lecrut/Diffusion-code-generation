from datetime import datetime, timedelta

class DayElapsedCalculator:
    def __init__(self, reference_time=None):
        self.reference_time = reference_time if reference_time else datetime.now()
        self.start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)

    def get_elapsed_seconds(self):
        delta = self.reference_time - self.start_of_day
        return int(delta.total_seconds())

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 1, 12, 30, 45)
    calculator = DayElapsedCalculator(sample_time)
    print(calculator.get_elapsed_seconds())