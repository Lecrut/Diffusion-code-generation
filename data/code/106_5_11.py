from datetime import date

class DateDifferenceCalculator:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def get_year_difference(self) -> int:
        return abs(self.end_date.year - self.start_date.year)

    def get_month_difference(self) -> int:
        return abs((self.end_date.year * 12 + self.end_date.month) - (self.start_date.year * 12 + self.start_date.month))

    def get_start_year(self) -> int:
        return self.start_date.year

    def get_end_year(self) -> int:
        return self.end_date.year

if __name__ == '__main__':
    start = date(1990, 1, 1)
    end = date(2023, 12, 31)
    calc = DateDifferenceCalculator(start, end)
    print(calc.get_year_difference())
    print(calc.get_month_difference())
    print(calc.get_start_year())
    print(calc.get_end_year())