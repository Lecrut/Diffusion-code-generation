from datetime import datetime, time

class TimeElapsedCalculator:
    FORMAT_STR = "%H:%M:%S"
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_midnight(reference_date):
        return datetime.combine(reference_date, time.min)

    def __init__(self, reference_time=None):
        if reference_time is None:
            self.reference_time = datetime.now()
        else:
            self.reference_time = reference_time

    def calculate(self):
        midnight = self.get_midnight(self.reference_time.date())
        delta = self.reference_time - midnight
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // self.SECONDS_PER_HOUR
        remaining_seconds = total_seconds % self.SECONDS_PER_HOUR
        minutes = remaining_seconds // self.SECONDS_PER_MINUTE
        seconds = remaining_seconds % self.SECONDS_PER_MINUTE
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_datetime = datetime(2023, 12, 25, 15, 30, 0)
    calculator = TimeElapsedCalculator(sample_datetime)
    output = calculator.calculate()
    print(output)