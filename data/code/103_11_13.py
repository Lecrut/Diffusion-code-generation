import time
import datetime

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE
DAYS_IN_WEEK = 7
HOURS_PER_DAY = 24

class TimeCalculator:
    def __init__(self):
        self._start_of_day_seconds = None

    def compute_seconds_since_start_of_day(self):
        now = datetime.datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed = now - start_of_day
        return elapsed.total_seconds()

def main():
    calculator = TimeCalculator()
    result = calculator.compute_seconds_since_start_of_day()
    print(result)

if __name__ == '__main__':
    main()