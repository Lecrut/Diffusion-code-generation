from datetime import date
import calendar

class DateDifferenceCalculator:
    DAYS_PER_YEAR = 365
    DAYS_PER_LEAP_YEAR = 366

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return calendar.isleap(year)

    @staticmethod
    def days_in_year(year: int) -> int:
        return 366 if DateDifferenceCalculator.is_leap_year(year) else 365

    def calculate_absolute_year_difference(self, date1: date, date2: date) -> int:
        if not isinstance(date1, date) or not isinstance(date2, date):
            raise ValueError("Inputs must be date objects")
        
        delta = date2 - date1
        total_days = abs(delta.days)
        
        if total_days == 0:
            return 0
        
        years = total_days // self.DAYS_PER_YEAR
        return years

if __name__ == '__main__':
    start_date = date(2020, 1, 1)
    end_date = date(2025, 1, 1)
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_absolute_year_difference(start_date, end_date)
    print(result)