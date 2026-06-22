import calendar
from datetime import date

class MonthCalculator:
    def days_in_month(self):
        today = date.today()
        _, num_days = calendar.monthrange(today.year, today.month)
        return num_days

if __name__ == '__main__':
    calculator = MonthCalculator()
    print(calculator.days_in_month())