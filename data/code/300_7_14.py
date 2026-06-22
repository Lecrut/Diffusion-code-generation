import calendar
from datetime import date

class DaysLeftInMonth:
    def days_left(self):
        today = date.today()
        _, num_days_in_month = calendar.monthrange(today.year, today.month)
        return num_days_in_month - today.day

if __name__ == '__main__':
    days_left_calculator = DaysLeftInMonth()
    print(days_left_calculator.days_left())