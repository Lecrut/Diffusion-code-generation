import datetime

class DateCalculator:
    def __init__(self):
        self.today = datetime.date.today()

    @staticmethod
    def days_in_month(year, month):
        if month == 12:
            return (datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)).days
        else:
            return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days

    def days_remaining_in_current_month(self):
        current_year = self.today.year
        current_month = self.today.month
        return DateCalculator.days_in_month(current_year, current_month) - (self.today.day - 1)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.days_remaining_in_current_month()
    print(result)