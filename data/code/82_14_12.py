class YearDifferenceCalculator:

    def calculate_difference(self, year1: int, year2: int) -> int:
        return abs(year1 - year2)
if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result1 = calculator.calculate_difference(2060, 2005)
    result2 = calculator.calculate_difference(1980, 2040)
    print(result1)
    print(result2)