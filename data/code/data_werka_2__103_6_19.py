import time

class TimeElapsedCalculator:
    def __init__(self):
        self.reference_time = time.time

    def calculate_seconds_since_midnight(self):
        current_timestamp = self.reference_time()
        local_time = time.localtime(current_timestamp)
        seconds_elapsed = (
            local_time.tm_hour * 3600 +
            local_time.tm_min * 60 +
            local_time.tm_sec
        )
        return seconds_elapsed

    def get_current_timestamp(self):
        return self.reference_time()

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    elapsed_seconds = calculator.calculate_seconds_since_midnight()
    current_ts = calculator.get_current_timestamp()
    print(elapsed_seconds)
    print(current_ts)