import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

class DayFractionCalculator:
    def __init__(self):
        self.seconds_per_hour = SECONDS_PER_HOUR
        self.seconds_per_day = SECONDS_PER_DAY

    def calculate(self):
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        elapsed_seconds = (hours * self.seconds_per_hour) + (minutes * 60) + seconds
        return elapsed_seconds / self.seconds_per_day

if __name__ == '__main__':
    calculator = DayFractionCalculator()
    result = calculator.calculate()
    print(result)