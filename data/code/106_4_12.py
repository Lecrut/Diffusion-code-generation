from datetime import date

class DateCalculator:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2

    def calculate_years_difference(self) -> int:
        return abs((self.date2 - self.date1).days // 365)

if __name__ == '__main__':
    calculator1 = DateCalculator(date(2020, 1, 1), date(2023, 4, 1))
    print(calculator1.calculate_years_difference())

    calculator2 = DateCalculator(date(2019, 12, 31), date(2020, 1, 1))
    print(calculator2.calculate_years_difference())