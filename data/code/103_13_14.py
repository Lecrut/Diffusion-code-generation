import time

class DayFractionCalculator:
    SECONDS_PER_HOUR = 3600
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    SECONDS_PER_DAY = HOURS_PER_DAY * SECONDS_PER_HOUR

    def __init__(self, reference_time=None):
        if reference_time is None:
            reference_time = time.localtime()
        self._time_struct = reference_time

    def get_elapsed_seconds(self):
        hours = self._time_struct.tm_hour
        minutes = self._time_struct.tm_min
        seconds = self._time_struct.tm_sec
        return (hours * self.SECONDS_PER_HOUR) + (minutes * self.MINUTES_PER_HOUR) + seconds

    def get_fraction(self):
        elapsed = self.get_elapsed_seconds()
        return elapsed / self.SECONDS_PER_DAY

    def get_remaining_fraction(self):
        fraction = self.get_fraction()
        return 1.0 - fraction

if __name__ == '__main__':
    calculator = DayFractionCalculator()
    fraction_passed = calculator.get_fraction()
    fraction_remaining = calculator.get_remaining_fraction()
    print(fraction_passed)
    print(fraction_remaining)