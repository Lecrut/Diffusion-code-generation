import calendar
from datetime import datetime

class DaysLeftCalculator:
    def days_left_in_month(self):
        today = datetime.now()
        _, last_day = calendar.monthrange(today.year, today.month)
        return last_day - today.day + 1

if __name__ == '__main__':
    calculator = DaysLeftCalculator()
    print(calculator.days_left_in_month())