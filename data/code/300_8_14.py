from dateutil.relativedelta import relativedelta
from datetime import datetime

class MonthDaysCalculator:
    MONTHS_WITH_31_DAYS = {1, 3, 5, 7, 8, 10, 12}

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(year, month):
        if month in MonthDaysCalculator.MONTHS_WITH_31_DAYS:
            return 31
        elif month == 2:
            return 29 if MonthDaysCalculator.is_leap_year(year) else 28
        else:
            return 30

    @staticmethod
    def days_remaining(year, month):
        today = datetime.now()
        target_date = datetime(year, month + 1, 1)
        delta = relativedelta(target_date, today)
        return delta.days
if __name__ == '__main__':
    year = 2023
    month = 4
    print(f'Days remaining in {year}-{month}: {MonthDaysCalculator.days_remaining(year, month)}')