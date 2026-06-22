import calendar
from datetime import date

class DaysLeftInMonth:
    def days_left(self):
        today = date.today()
        _, last_day = calendar.monthrange(today.year, today.month)
        return last_day - today.day

if __name__ == '__main__':
    calculator = DaysLeftInMonth()
    print(calculator.days_left())