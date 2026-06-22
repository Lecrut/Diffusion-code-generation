class YearDifferenceCalculator:
    def __init__(self, year1: int, year2: int) -> None:
        self.year1 = year1
        self.year2 = year2

    def calculate(self) -> int:
        return abs(self.year1 - self.year2)

    def get_details(self) -> str:
        return f"{self.year1} and {self.year2}"

if __name__ == '__main__':
    calc = YearDifferenceCalculator(2023, 2010)
    print(calc.calculate())
    print(calc.get_details())
    calc2 = YearDifferenceCalculator(1999, 2023)
    print(calc2.calculate())