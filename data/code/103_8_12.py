import time

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE

class TimeCalculator:
    def __init__(self):
        self.localtime = time.localtime

    def get_elapsed_seconds_today(self) -> int:
        now = self.localtime()
        hours = now.tm_hour
        minutes = now.tm_min
        seconds = now.tm_sec
        total_seconds = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds
        return total_seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.get_elapsed_seconds_today()
    print(result)