class DayElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, reference_date):
        self.reference_date = reference_date

    def _get_start_of_day(self):
        return self.reference_date.replace(hour=0, minute=0, second=0, microsecond=0)

    def _get_seconds_since_start(self):
        start = self._get_start_of_day()
        delta = self.reference_date - start
        return int(delta.total_seconds())

    def calculate(self):
        total_seconds = self._get_seconds_since_start()
        hours = total_seconds // self.SECONDS_PER_HOUR
        remaining_seconds = total_seconds % self.SECONDS_PER_HOUR
        minutes = remaining_seconds // self.SECONDS_PER_MINUTE
        seconds = remaining_seconds % self.SECONDS_PER_MINUTE
        return {
            "total_seconds": total_seconds,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 11, 15, 10, 20, 30)
    calculator = DayElapsedCalculator(sample_date)
    result = calculator.calculate()
    print(result)