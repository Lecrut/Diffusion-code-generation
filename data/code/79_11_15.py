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
            return date(year, month, 1)
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = date(2023, 11, 30)
    print(calculator.next_month(sample_date))