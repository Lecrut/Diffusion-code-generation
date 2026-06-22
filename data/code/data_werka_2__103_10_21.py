from datetime import datetime, time

class DayElapsedCalculator:
    def __init__(self, reference_datetime):
        self.reference_datetime = reference_datetime

    def get_start_of_day(self):
        return datetime.combine(self.reference_datetime.date(), time.min)

    def get_elapsed_seconds(self):
        start = self.get_start_of_day()
        delta = self.reference_datetime - start
        return delta.total_seconds()

    def get_formatted_elapsed(self):
        total_secs = int(self.get_elapsed_seconds())
        hours = total_secs // 3600
        minutes = (total_secs % 3600) // 60
        seconds = total_secs % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 45)
    calculator = DayElapsedCalculator(sample_dt)
    start = calculator.get_start_of_day()
    secs = calculator.get_elapsed_seconds()
    fmt = calculator.get_formatted_elapsed()
    print(f"Start: {start}")
    print(f"Elapsed Seconds: {secs}")
    print(f"Elapsed Formatted: {fmt}")