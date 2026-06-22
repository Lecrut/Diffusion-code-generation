from datetime import datetime, timedelta

class DayTimeCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def get_start_of_day(date_obj):
        return date_obj.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def calculate_elapsed_seconds(start_dt, end_dt):
        delta = end_dt - start_dt
        return int(delta.total_seconds())

    def __init__(self, reference_date):
        self.reference_date = reference_date
        self.start_of_day = self.get_start_of_day(reference_date)
        self.elapsed_seconds = self.calculate_elapsed_seconds(self.start_of_day, reference_date)

    def get_formatted_elapsed(self):
        hours = self.elapsed_seconds // self.SECONDS_PER_HOUR
        remainder = self.elapsed_seconds % self.SECONDS_PER_HOUR
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        return f"{hours}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    calculator = DayTimeCalculator(sample_date)
    print(calculator.get_formatted_elapsed())