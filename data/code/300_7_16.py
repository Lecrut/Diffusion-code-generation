import calendar
from datetime import datetime

class DaysLeftInMonth:
    def days_left(self):
        today = datetime.now()
        _, last_day = calendar.monthrange(today.year, today.month)
        return last_day - today.day

if __name__ == '__main__':
    days_left_calculator = DaysLeftInMonth()
    print(days_left_calculator.days_left())