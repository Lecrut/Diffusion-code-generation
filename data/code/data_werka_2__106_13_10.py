import datetime
import calendar

class YearDifferenceCalculator:
    def __init__(self, timestamp_a: int, timestamp_b: int):
        self.ts_a = timestamp_a
        self.ts_b = timestamp_b

    def calculate(self) -> int:
        dt_a = datetime.datetime.utcfromtimestamp(self.ts_a)
        dt_b = datetime.datetime.utcfromtimestamp(self.ts_b)
        return abs(dt_a.year - dt_b.year)

    def get_years(self) -> tuple:
        dt_a = datetime.datetime.utcfromtimestamp(self.ts_a)
        dt_b = datetime.datetime.utcfromtimestamp(self.ts_b)
        return (dt_a.year, dt_b.year)

    def is_same_year(self) -> bool:
        return self.calculate() == 0

if __name__ == '__main__':
    calc = YearDifferenceCalculator(1609459200, 1640995200)
    print(calc.calculate())
    print(calc.get_years())
    print(calc.is_same_year())