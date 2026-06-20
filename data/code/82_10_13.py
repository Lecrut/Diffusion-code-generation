class YearDifferenceCalculator:
    def calculate_difference(self, year1: int, year2: int) -> int:
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.calculate_difference(2023, 1985)
    print(result)