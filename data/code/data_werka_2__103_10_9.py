import datetime

TIME_UNITS = {
    "day": 86400,
    "hour": 3600,
    "minute": 60,
    "second": 1
}

class DayElapsedCalculator:
    def __init__(self, reference_date):
        if not isinstance(reference_date, datetime.datetime):
            raise ValueError("reference_date must be a datetime object")
        self.reference_date = reference_date

    def get_elapsed_seconds(self):
        start_of_day = self.reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = self.reference_date - start_of_day
        return int(delta.total_seconds())

    def format_elapsed(self):
        seconds_total = self.get_elapsed_seconds()
        hours = seconds_total // TIME_UNITS["hour"]
        remainder = seconds_total % TIME_UNITS["hour"]
        minutes = remainder // TIME_UNITS["minute"]
        seconds = remainder % TIME_UNITS["minute"]
        return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
    calculator = DayElapsedCalculator(sample_dt)
    result = calculator.format_elapsed()
    print(result)