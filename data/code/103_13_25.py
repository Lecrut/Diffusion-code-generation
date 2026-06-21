import time
import math

SECONDS_PER_HOUR = 3600
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
SECONDS_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR * MINUTES_PER_HOUR

class DayFractionCalculator:
    def __init__(self):
        self.seconds_per_day = SECONDS_PER_DAY

    def get_fraction(self):
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        microsecond = now.tm_usec

        total_seconds_elapsed = (hour * SECONDS_PER_HOUR) + (minute * MINUTES_PER_HOUR) + second + (microsecond / 1000000.0)
        fraction = total_seconds_elapsed / self.seconds_per_day
        return fraction

if __name__ == '__main__':
    calculator = DayFractionCalculator()
    fraction = calculator.get_fraction()
    print(fraction)