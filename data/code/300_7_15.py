import calendar
from datetime import datetime

class MonthDaysCalculator:
    def remaining_days(self):
        now = datetime.now()
        _, last_day = calendar.monthrange(now.year, now.month)
        return last_day - now.day

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.remaining_days())