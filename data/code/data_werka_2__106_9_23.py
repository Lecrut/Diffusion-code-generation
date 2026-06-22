from datetime import date

class DateCalculator:
    def __init__(self, start_year: int, end_year: int, start_month: int = 1, start_day: int = 1, end_month: int = 1, end_day: int = 1):
        self.start_date = date(start_year, start_month, start_day)
        self.end_date = date(end_year, end_month, end_day)

    def compute_year_difference(self) -> int:
        full_years = self.end_date.year - self.start_date.year
        if self.end_date.month < self.start_date.month:
            full_years -= 1
        elif self.end_date.month == self.start_date.month:
            if self.end_date.day < self.start_date.day:
                full_years -= 1
        return full_years

    def get_dates(self) -> tuple:
        return (self.start_date, self.end_date)

if __name__ == '__main__':
    calc = DateCalculator(2018, 2023, 12, 25, 1, 1)
    diff = calc.compute_year_difference()
    dates = calc.get_dates()
    print(diff)
    print(dates)