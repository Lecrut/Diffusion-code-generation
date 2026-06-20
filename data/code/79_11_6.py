from datetime import date, timedelta

class DateCalculator:

    def next_month(self, input_date):
        year = input_date.year
        month = input_date.month
        day = input_date.day
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        try:
            return date(year, month, day)
        except ValueError:
            if month == 2 and day > 28:
                return date(year, month, 28)
            elif month in [4, 6, 9, 11] and day > 30:
                return date(year, month, 30)
            else:
                raise
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = date(2023, 10, 31)
    next_month_date = calculator.next_month(sample_date)
    print(next_month_date)