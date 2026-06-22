from datetime import date
import calendar

class DateCalculator:
    DAYS_IN_YEAR = 365
    DAYS_IN_LEAP_YEAR = 366

    @staticmethod
    def is_leap_year(year):
        return calendar.isleap(year)

    @staticmethod
    def days_in_month(year, month):
        if month == 2:
            return 29 if DateCalculator.is_leap_year(year) else 28
        if month in (4, 6, 9, 11):
            return 30
        return 31

    def compute_year_difference(self, start_date: date, end_date: date) -> int:
        if start_date > end_date:
            return -self.compute_year_difference(end_date, start_date)
        
        years = end_date.year - start_date.year
        start_month_day = (start_date.month, start_date.day)
        end_month_day = (end_date.month, end_date.day)
        
        if end_month_day < start_month_day:
            years -= 1
            
        return years

if __name__ == '__main__':
    calc = DateCalculator()
    d_start = date(2019, 11, 30)
    d_end = date(2024, 11, 29)
    diff = calc.compute_year_difference(d_start, d_end)
    print(diff)