import time

class TimeElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def _get_current_timestamp():
        return time.time()

    @staticmethod
    def _get_today_start_timestamp(current_timestamp):
        return current_timestamp - (current_timestamp % 86400)

    def __init__(self):
        self.current_timestamp = self._get_current_timestamp()
        self.today_start = self._get_today_start_timestamp(self.current_timestamp)
        self.elapsed_seconds = self.current_timestamp - self.today_start

    def get_elapsed_hours(self):
        return int(self.elapsed_seconds // self.SECONDS_PER_HOUR)

    def get_elapsed_minutes(self):
        remaining_after_hours = self.elapsed_seconds % self.SECONDS_PER_HOUR
        return int(remaining_after_hours // self.SECONDS_PER_MINUTE)

    def get_elapsed_seconds(self):
        remaining_after_minutes = self.elapsed_seconds % self.SECONDS_PER_MINUTE
        return int(remaining_after_minutes)

    def get_elapsed_tuple(self):
        hours = self.get_elapsed_hours()
        minutes = self.get_elapsed_minutes()
        seconds = self.get_elapsed_seconds()
        return (hours, minutes, seconds)

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    result = calculator.get_elapsed_tuple()
    print(result)