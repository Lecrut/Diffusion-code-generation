import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
SECONDS_IN_DAY = 86400

class TimeElapsedCalculator:
    def __init__(self):
        self.current_time = time.time()

    def calculate_since_midnight(self):
        seconds_since_epoch = self.current_time
        seconds_into_day = seconds_since_epoch % SECONDS_IN_DAY
        hours = int(seconds_into_day // SECONDS_IN_HOUR)
        remaining_seconds = seconds_into_day % SECONDS_IN_HOUR
        minutes = int(remaining_seconds // SECONDS_IN_MINUTE)
        seconds = int(remaining_seconds % SECONDS_IN_MINUTE)
        return hours, minutes, seconds

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    result = calculator.calculate_since_midnight()
    print(result)