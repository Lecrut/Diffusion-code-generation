from datetime import datetime, timedelta

class MonthDurationCalculator:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.start_date = datetime(year, month, 1)
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        self.end_date = datetime(next_year, next_month, 1) - timedelta(seconds=1)

    def get_total_duration(self) -> timedelta:
        return self.end_date - self.start_date

    def get_remaining_time(self, current_time: datetime) -> timedelta:
        if current_time < self.start_date:
            return self.get_total_duration()
        if current_time > self.end_date:
            return timedelta(0)
        return self.end_date - current_time

    def get_elapsed_time(self, current_time: datetime) -> timedelta:
        if current_time < self.start_date:
            return timedelta(0)
        if current_time > self.end_date:
            return self.get_total_duration()
        return current_time - self.start_date

if __name__ == '__main__':
    calculator = MonthDurationCalculator(2023, 10)
    sample_time = datetime(2023, 10, 15, 12, 0, 0)
    total = calculator.get_total_duration()
    remaining = calculator.get_remaining_time(sample_time)
    elapsed = calculator.get_elapsed_time(sample_time)
    print(total)
    print(remaining)
    print(elapsed)