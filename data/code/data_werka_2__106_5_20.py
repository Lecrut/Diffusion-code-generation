from datetime import date

class DateAnalyzer:
    def __init__(self, d1: date, d2: date):
        self.d1 = d1
        self.d2 = d2

    def year_difference(self) -> int:
        return abs(self.d1.year - self.d2.year)

    def is_same_month(self) -> bool:
        return self.d1.month == self.d2.month

    def days_between(self) -> int:
        return abs((self.d1 - self.d2).days)

if __name__ == '__main__':
    start_date = date(1990, 1, 1)
    end_date = date(2023, 12, 31)
    analyzer = DateAnalyzer(start_date, end_date)
    print(analyzer.year_difference())
    print(analyzer.is_same_month())
    print(analyzer.days_between())