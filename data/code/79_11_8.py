from datetime import datetime, timedelta

class DateCalculator:

    def next_month(self, date):
        year = date.year
        month = date.month
        day = date.day
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        try:
            return datetime(year, month, day)
        except ValueError:
            return datetime(year, month, 1)
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = datetime(2023, 10, 15)
    next_month_date = calculator.next_month(sample_date)
    print(next_month_date)