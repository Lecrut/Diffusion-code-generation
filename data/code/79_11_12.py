from datetime import date, timedelta

class DateCalculator:

    def get_next_month(self, input_date):
        year = input_date.year
        month = input_date.month
        day = input_date.day
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        try:
            return date(next_year, next_month, day)
        except ValueError:
            if month == 2 and day > 28:
                return date(next_year, next_month, 28)
            elif month in [4, 6, 9, 11] and day > 30:
                return date(next_year, next_month, 30)
            else:
                raise
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = date(2023, 11, 30)
    print(calculator.get_next_month(sample_date))