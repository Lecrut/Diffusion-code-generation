from datetime import date, timedelta

class DateCalculator:
    BASE_YEAR = 2024
    BASE_MONTH = 7
    BASE_DAY = 4
    DAYS_TO_ADD = 30

    @staticmethod
    def calculate_future_date(year, month, day, days_to_add):
        start = date(year, month, day)
        delta = timedelta(days=days_to_add)
        return start + delta

    @staticmethod
    def format_date(d):
        return d.strftime("%Y-%m-%d")

if __name__ == '__main__':
    result_date = DateCalculator.calculate_future_date(
        DateCalculator.BASE_YEAR,
        DateCalculator.BASE_MONTH,
        DateCalculator.BASE_DAY,
        DateCalculator.DAYS_TO_ADD
    )
    print(DateCalculator.format_date(result_date))