from datetime import datetime, timedelta

class DayTimeCalculator:
    def __init__(self, reference_date):
        if not isinstance(reference_date, datetime):
            raise ValueError("reference_date must be a datetime object")
        self.reference_date = reference_date

    def get_start_of_day(self):
        return self.reference_date.replace(hour=0, minute=0, second=0, microsecond=0)

    def get_elapsed_seconds(self):
        start = self.get_start_of_day()
        delta = self.reference_date - start
        return int(delta.total_seconds())

    def get_elapsed_formatted(self):
        total_seconds = self.get_elapsed_seconds()
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    calculator = DayTimeCalculator(sample_date)
    print(calculator.get_elapsed_formatted())
    print(calculator.get_elapsed_seconds())