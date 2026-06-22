import datetime

class TimeElapsedCalculator:
    def __init__(self):
        self.reference_time = datetime.datetime.now()
        self.midnight = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        self.elapsed = self.reference_time - self.midnight
        self.total_seconds = self.elapsed.total_seconds()

    def get_total_seconds(self):
        return self.total_seconds

    def get_hours(self):
        return self.total_seconds / 3600

    def get_minutes(self):
        return self.total_seconds / 60

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    print(calculator.get_total_seconds())
    print(calculator.get_hours())
    print(calculator.get_minutes())