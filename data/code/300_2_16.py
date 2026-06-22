import dateutil.relativedelta

class DateCalculator:
    @staticmethod
    def get_last_day_of_month(year, month):
        return (dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(day=1)) - dateutil.relativedelta.relativedelta(days=1)

    @staticmethod
    def calculate_remaining_days(year, month):
        last_day = DateCalculator.get_last_day_of_month(year, month)
        today = dateutil.relativedelta.relativedelta.today()
        return (last_day - today).days

if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    result1 = calculator.calculate_remaining_days(year1, month1)
    print(f"Remaining days in {year1}-{month1:02d}: {result1}")