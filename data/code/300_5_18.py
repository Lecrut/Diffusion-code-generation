import calendar
from datetime import date

class DaysLeftCalculator:
    @staticmethod
    def days_left_in_month():
        today = date.today()
        year, month, _ = today.year, today.month, today.day
        _, num_days = calendar.monthrange(year, month)
        return num_days - day

if __name__ == '__main__':
    calculator = DaysLeftCalculator()
    print(calculator.days_left_in_month())