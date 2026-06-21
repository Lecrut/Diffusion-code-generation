import datetime

class TimeCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def _get_current_datetime():
        return datetime.datetime.now()

    @staticmethod
    def _normalize_to_start_of_day(dt):
        return datetime.datetime.min.replace(year=dt.year, month=dt.month, day=dt.day)

    def get_elapsed_seconds(self):
        current = self._get_current_datetime()
        start = self._normalize_to_start_of_day(current)
        delta = current - start
        return delta.total_seconds()

    def get_formatted_elapsed(self):
        seconds = self.get_elapsed_seconds()
        hours = int(seconds) // TimeCalculator.SECONDS_PER_HOUR
        remaining = int(seconds) % TimeCalculator.SECONDS_PER_HOUR
        minutes = remaining // TimeCalculator.SECONDS_PER_MINUTE
        secs = remaining % TimeCalculator.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.get_formatted_elapsed()
    print(result)