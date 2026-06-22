import datetime

class DaysRemainingCalculator:
    def __init__(self):
        today = datetime.date.today()
        self.current_year = today.year
        self.current_month = today.month
        _, self.days_in_current_month = calendar.monthrange(self.current_year, self.current_month)

    def get_days_remaining(self) -> int:
        today = datetime.date.today()
        last_day_of_month = datetime.date(self.current_year, self.current_month, self.days_in_current_month)
        days_remaining = (last_day_of_month - today).days
        return days_remaining

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    remaining_days = calculator.get_days_remaining()
    print(f"Days remaining in this month: {remaining_days}")