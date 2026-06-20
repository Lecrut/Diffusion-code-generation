from datetime import date

class MonthDaysCalculator:
    def __init__(self):
        self.today = date.today()

    @staticmethod
    def month_range(year, month):
        _, num_days = calendar.monthrange(year, month)
        return num_days

    def days_left(self):
        year, month = self.today.year, self.today.month
        last_day = MonthDaysCalculator.month_range(year, month)
        return (date(year, month, last_day) - self.today).days + 1

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.days_left())