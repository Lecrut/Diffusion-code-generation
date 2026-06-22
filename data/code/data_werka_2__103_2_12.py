import time

class TimeElapsedCalculator:
    def __init__(self):
        self.reference_point = None

    def _get_midnight_timestamp(self, timestamp):
        seconds_into_day = timestamp % 86400
        return timestamp - seconds_into_day

    def calculate_elapsed(self):
        current_time = time.time()
        midnight = self._get_midnight_timestamp(current_time)
        elapsed_seconds = current_time - midnight
        hours = int(elapsed_seconds // 3600)
        remainder = elapsed_seconds % 3600
        minutes = int(remainder // 60)
        seconds = int(remainder % 60)
        self.reference_point = current_time
        return hours, minutes, seconds

    def get_reference_time(self):
        return self.reference_point

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    h, m, s = calculator.calculate_elapsed()
    print(f"{h} hours, {m} minutes, {s} seconds")
    print(calculator.get_reference_time())