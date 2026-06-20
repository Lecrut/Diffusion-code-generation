import datetime

class DateCalculator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def days_between(self):
        delta = self.end_date - self.start_date
        return abs(delta.days)

if __name__ == '__main__':
    calculator = DateCalculator(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    print(f"Days between January 1, 2023 and December 31, 2023: {calculator.days_between()}")