import time

class TimeElapsedCalculator:
    def __init__(self):
        self._reference_now = None

    def compute(self):
        current_time = time.time()
        self._reference_now = current_time
        seconds_since_midnight = current_time % 86400
        total_hours = int(seconds_since_midnight // 3600)
        remaining_seconds = seconds_since_midnight - (total_hours * 3600)
        total_minutes = int(remaining_seconds // 60)
        total_seconds = int(remaining_seconds % 60)
        return total_hours, total_minutes, total_seconds

    def get_reference_time(self):
        if self._reference_now is None:
            raise ValueError("Compute must be called first")
        return self._reference_now

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    hours, minutes, seconds = calculator.compute()
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
    ref = calculator.get_reference_time()
    print(ref)