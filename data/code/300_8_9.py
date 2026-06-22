from dateutil.relativedelta import relativedelta
from datetime import date

class MonthDays:

    def days_remaining(self, year, month):
        current_date = date(year, month, 1)
        next_month = date(year, month + 1, 1) if month < 12 else date(year + 1, 1, 1)
        remaining_days = (next_month - current_date).days
        return remaining_days
if __name__ == '__main__':
    month_calculator = MonthDays()
    print(month_calculator.days_remaining(2023, 1))
    print(month_calculator.days_remaining(2023, 2))
    print(month_calculator.days_remaining(2023, 3))
    print(month_calculator.days_remaining(2023, 4))
    print(month_calculator.days_remaining(2023, 5))
    print(month_calculator.days_remaining(2023, 6))
    print(month_calculator.days_remaining(2023, 7))
    print(month_calculator.days_remaining(2023, 8))
    print(month_calculator.days_remaining(2023, 9))
    print(month_calculator.days_remaining(2023, 10))