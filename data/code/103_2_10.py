import time
import math

class TimeElapsedCalculator:
    def __init__(self):
        self.seconds_per_hour = 3600
        self.seconds_per_minute = 60

    def calculate_elapsed_since_midnight(self):
        current_timestamp = time.time()
        start_of_day_timestamp = current_timestamp - (current_timestamp % 86400)
        elapsed_seconds = current_timestamp - start_of_day_timestamp
        hours = int(elapsed_seconds // self.seconds_per_hour)
        remaining_seconds = elapsed_seconds % self.seconds_per_hour
        minutes = int(remaining_seconds // self.seconds_per_minute)
        seconds = int(remaining_seconds % self.seconds_per_minute)
        return hours, minutes, seconds

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    result = calculator.calculate_elapsed_since_midnight()
    print(result)