import datetime

class DayElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60

    @staticmethod
    def _get_start_of_day(dt):
        return datetime.datetime.min.replace(year=dt.year, month=dt.month, day=dt.day)

    def __init__(self):
        self.now = datetime.datetime.now()

    def calculate_elapsed(self):
        start = self._get_start_of_day(self.now)
        delta = self.now - start
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // self.SECONDS_PER_HOUR
        remaining = total_seconds % self.SECONDS_PER_HOUR
        minutes = remaining // self.SECONDS_PER_MINUTE
        seconds = remaining % self.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    calculator = DayElapsedCalculator()
    print(calculator.calculate_elapsed())