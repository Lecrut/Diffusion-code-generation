from datetime import datetime

class DateCalculator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def calculate_days(self) -> int:
        delta = self.end_date - self.start_date
        return delta.days

    def get_dates(self):
        return (self.start_date.strftime('%Y-%m-%d'), self.end_date.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    calc = DateCalculator('2020-01-01', '2020-12-31')
    days = calc.calculate_days()
    dates = calc.get_dates()
    print(days)
    print(dates)