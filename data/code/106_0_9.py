from datetime import datetime
from calendar import isleap

class DateDiffCalculator:
    def __init__(self, start_year: int, start_month: int, start_day: int,
                 end_year: int, end_month: int, end_day: int):
        self.start_date = datetime(start_year, start_month, start_day)
        self.end_date = datetime(end_year, end_month, end_day)

    def calculate_full_years(self) -> int:
        years = self.end_date.year - self.start_date.year
        if self.end_date.month < self.start_date.month:
            years -= 1
        elif self.end_date.month == self.start_date.month:
            if self.end_date.day < self.start_date.day:
                years -= 1
        return years

    def is_leap_year(self, year: int) -> bool:
        return isleap(year)

    def get_days_in_month(self, year: int, month: int) -> int:
        if month == 2:
            return 29 if isleap(year) else 28
        days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_months[month]

if __name__ == '__main__':
    calculator = DateDiffCalculator(2000, 2, 29, 2024, 2, 28)
    years_diff = calculator.calculate_full_years()
    start_leap = calculator.is_leap_year(2000)
    end_leap = calculator.is_leap_year(2024)
    days_in_feb_2000 = calculator.get_days_in_month(2000, 2)
    print(years_diff)
    print(start_leap)
    print(end_leap)
    print(days_in_feb_2000)