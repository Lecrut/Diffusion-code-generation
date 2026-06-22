import calendar

class YearDifferenceCalculator:
    def __init__(self, timestamp_a: int, timestamp_b: int):
        self.timestamp_a = timestamp_a
        self.timestamp_b = timestamp_b

    def get_absolute_year_difference(self) -> int:
        year_a = calendar.gmtime(self.timestamp_a).tm_year
        year_b = calendar.gmtime(self.timestamp_b).tm_year
        return abs(year_a - year_b)

    def get_signed_year_difference(self) -> int:
        year_a = calendar.gmtime(self.timestamp_a).tm_year
        year_b = calendar.gmtime(self.timestamp_b).tm_year
        return year_b - year_a

if __name__ == '__main__':
    calc = YearDifferenceCalculator(1640995200, 1609459200)
    print(calc.get_absolute_year_difference())
    print(calc.get_signed_year_difference())