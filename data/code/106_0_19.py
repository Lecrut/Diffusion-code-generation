from datetime import date
import calendar

class DateDifferenceCalculator:
    YEAR_DIVISOR = 365.2425

    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def calculate_days_between(self) -> int:
        delta = self.end_date - self.start_date
        return delta.days

    def calculate_approximate_years(self) -> float:
        days = self.calculate_days_between()
        return days / self.YEAR_DIVISOR

    def calculate_exact_year_difference(self) -> int:
        years = self.end_date.year - self.start_date.year
        if self.end_date.month < self.start_date.month:
            years -= 1
        elif self.end_date.month == self.start_date.month:
            if self.end_date.day < self.start_date.day:
                years -= 1
        if self.start_date > self.end_date:
            years = -years
        return years

    def get_leap_year_count(self) -> int:
        start_y = self.start_date.year
        end_y = self.end_date.year
        def count_leaps(y):
            return y // 4 - y // 100 + y // 400
        return count_leaps(end_y) - count_leaps(start_y - 1)

if __name__ == '__main__':
    d1 = date(2000, 2, 29)
    d2 = date(2024, 2, 28)
    calc = DateDifferenceCalculator(d1, d2)
    print(calc.calculate_exact_year_difference())
    print(calc.get_leap_year_count())