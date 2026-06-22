import datetime
import time

class TimeProgression:
    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.datetime.now()
        else:
            self.reference_time = reference_time

    def get_seconds_passed(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return delta.total_seconds()

    def get_fractional_day(self):
        seconds_passed = self.get_seconds_passed()
        return seconds_passed / 86400

    def get_microseconds_passed(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return delta.microseconds + (delta.seconds * 1000000)

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 5, 12, 30, 45, 123456)
    calculator = TimeProgression(sample_time)
    print(calculator.get_seconds_passed())
    print(calculator.get_fractional_day())
    print(calculator.get_microseconds_passed())