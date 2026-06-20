from datetime import date

class YearDifferenceCalculator:
    def __init__(self, year1: int, year2: int):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self) -> int:
        return abs(self.year2 - self.year1)

if __name__ == '__main__':
    calculator1 = YearDifferenceCalculator(2023, 1998)
    print(calculator1.calculate_difference())

    calculator2 = YearDifferenceCalculator(2010, 2023)
    print(calculator2.calculate_difference())