from datetime import datetime

class MonthFractionCalculator:

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.current_time = datetime.now()
        self.month_start = datetime(year, month, 1)
        self.days_in_month = self._get_days_in_month(year, month)
        self.month_end = datetime(year, month, self.days_in_month, 23, 59, 59)

    def _get_days_in_month(self, year: int, month: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month in [4, 6, 9, 11]:
            return 30
        if month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return 29
            return 28
        return 0

    def calculate_remaining_fraction(self) -> float:
        if self.current_time < self.month_start:
            return 1.0
        if self.current_time > self.month_end:
            return 0.0
        elapsed_seconds = (self.current_time - self.month_start).total_seconds()
        total_seconds = (self.month_end - self.month_start).total_seconds()
        if total_seconds == 0:
            return 0.0
        remaining_seconds = total_seconds - elapsed_seconds
        return remaining_seconds / total_seconds

    def get_month_info(self) -> dict:
        return {'year': self.year, 'month': self.month, 'days_in_month': self.days_in_month, 'start_date': self.month_start, 'end_date': self.month_end, 'current_time': self.current_time}
if __name__ == '__main__':
    calc1 = MonthFractionCalculator(2023, 10)
    print(f'Current month remaining fraction: {calc1.calculate_remaining_fraction():.4f}')
    print(f'Month info: {calc1.get_month_info()}')
    calc2 = MonthFractionCalculator(2024, 12)
    print(f'Future month remaining fraction: {calc2.calculate_remaining_fraction():.4f}')
    calc3 = MonthFractionCalculator(2020, 2)
    print(f'Past month remaining fraction: {calc3.calculate_remaining_fraction():.4f}')
    calc4 = MonthFractionCalculator(2024, 2)
    print(f'Leap year February remaining fraction: {calc4.calculate_remaining_fraction():.4f}')
    print(f'Days in Feb 2024: {calc4.days_in_month}')