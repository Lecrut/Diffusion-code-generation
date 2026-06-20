import datetime

class DateCalculator:
    def __init__(self, start_date):
        self.start_date = start_date

    def get_next_month_date(self):
        if self.start_date.month == 12:
            year = self.start_date.year + 1
            month = 1
        else:
            year = self.start_date.year
            month = self.start_date.month + 1
        
        day = min(self.start_date.day, [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime.datetime(year, month, day)

if __name__ == '__main__':
    calculator = DateCalculator(datetime.date(2023, 1, 15))
    next_month_date = calculator.get_next_month_date()
    print(next_month_date.strftime('%Y-%m-%d'))