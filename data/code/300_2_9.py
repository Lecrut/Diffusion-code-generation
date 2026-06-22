from dateutil.relativedelta import relativedelta

class DateCalculator:
    def calculate_remaining_days(self, year, month):
        from datetime import date
        today = date.today()
        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)
        remaining_days = relativedelta(next_month, today).days
        return remaining_days

if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    result1 = calculator.calculate_remaining_days(year1, month1)
    print(f"Remaining days from {year1}-{month1:02d}: {result1}")