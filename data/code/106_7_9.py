from datetime import date

class YearCalculator:
    ANNUAL_DAYS_OFFSET = date(2000, 1, 1)
    DAYS_PER_YEAR = 365.2425

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __init__(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("start_date must be before or equal to end_date")
        self.start_date = start_date
        self.end_date = end_date

    def compute_years(self):
        y1 = self.start_date.year
        y2 = self.end_date.year
        m1 = self.start_date.month
        d1 = self.start_date.day
        m2 = self.end_date.month
        d2 = self.end_date.day

        if y2 == y1:
            return 0

        if m2 < m1 or (m2 == m1 and d2 < d1):
            return y2 - y1 - 1
        return y2 - y1

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    calc = YearCalculator(start, end)
    result = calc.compute_years()
    print(result)