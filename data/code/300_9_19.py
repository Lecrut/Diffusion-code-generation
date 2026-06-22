import datetime

class DateCalculator:
    def calculate_days_remaining(self) -> int:
        today = datetime.date.today()
        last_day_of_month = datetime.date(today.year, today.month, 1) + datetime.timedelta(days=32)
        last_day_of_month -= datetime.timedelta(days=last_day_of_month.day)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    calculator = DateCalculator()
    remaining_days = calculator.calculate_days_remaining()
    print(f"Days remaining in the current month: {remaining_days}")