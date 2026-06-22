class TimeDeltaCalculator:
    def __init__(self, start_timestamp, end_timestamp):
        self._validate_input(start_timestamp)
        self._validate_input(end_timestamp)
        self.start = float(start_timestamp)
        self.end = float(end_timestamp)

    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Timestamps must be numeric types (int or float)")

    def get_difference_in_hours(self):
        delta_seconds = self.end - self.start
        return delta_seconds / 3600.0

if __name__ == '__main__':
    start_ts = 1700000000
    end_ts = 1700003600
    calculator = TimeDeltaCalculator(start_ts, end_ts)
    result = calculator.get_difference_in_hours()
    print(result)