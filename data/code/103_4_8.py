import datetime
import time

class DayFractionCalculator:
    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.datetime.now()
        else:
            self.reference_time = reference_time

    def get_fractional_day(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        seconds_in_day = 24 * 60 * 60
        return delta.total_seconds() / seconds_in_day

    def get_seconds_passed(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return delta.total_seconds()

    def get_microseconds_passed(self):
        start_of_day = self.reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_time - start_of_day
        return delta.total_seconds() * 1000000

if __name__ == '__main__':
    calc = DayFractionCalculator(datetime.datetime(2023, 10, 5, 12, 30, 45, 123456))
    print(calc.get_fractional_day())
    print(calc.get_seconds_passed())
    print(calc.get_microseconds_passed())