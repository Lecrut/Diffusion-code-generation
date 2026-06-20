from datetime import datetime

class TimeCalculator:
    def validate_times(self, time1: datetime, time2: datetime):
        if not isinstance(time1, datetime) or not isinstance(time2, datetime):
            raise ValueError("Both inputs must be datetime objects.")
        if time1 > time2:
            raise ValueError("The first time cannot be later than the second time.")

    def calculate_difference(self, time1: datetime, time2: datetime) -> timedelta:
        self.validate_times(time1, time2)
        return abs(time2 - time1)

if __name__ == '__main__':
    calculator = TimeCalculator()
    sample_start = datetime(2023, 10, 1, 12, 0, 0)
    sample_end = datetime(2023, 10, 1, 14, 30, 0)
    difference = calculator.calculate_difference(sample_start, sample_end)
    print(difference)