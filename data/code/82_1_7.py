class YearDifferenceCalculator:
    def calculate(self, year1: int, year2: int) -> int:
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.calculate(2024, 1999)
    print(result)