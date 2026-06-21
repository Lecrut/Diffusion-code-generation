import calendar
from datetime import datetime

class MonthCalculator:
    DAYS_IN_WEEK = 7
    MONTHS_IN_YEAR = 12

    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def is_leap_year(year):
        return calendar.isleap(year)

    @staticmethod
    def calculate_days_left(year, month, day):
        last_day = MonthCalculator.get_days_in_month(year, month)
        return last_day - day

if __name__ == '__main__':
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    
    days_left = MonthCalculator.calculate_days_left(current_year, current_month, current_day)
    print(days_left)