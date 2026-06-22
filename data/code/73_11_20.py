class TimeDeltaCalculator:
    def __init__(self, start_timestamp, end_timestamp):
        if not isinstance(start_timestamp, (int, float)):
            raise ValueError("start_timestamp must be numeric")
        if not isinstance(end_timestamp, (int, float)):
            raise ValueError("end_timestamp must be numeric")
        self.start = start_timestamp
        self.end = end_timestamp

    def get_difference_seconds(self):
        return self.end - self.start

    def get_difference_hours(self):
        seconds = self.get_difference_seconds()
        return seconds / 3600.0

if __name__ == '__main__':
    calc = TimeDeltaCalculator(1609459200, 1609462800)
    print(calc.get_difference_hours())
    print(calc.get_difference_seconds())