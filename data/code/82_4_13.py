class YearDifferenceCalculator:

    def calculate_difference(self, year1: int, year2: int) -> int:
        return year1 - year2
if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result1 = calculator.calculate_difference(2023, 1990)
    print(result1)
    result2 = calculator.calculate_difference(2020, 2020)
    print(result2)
    result3 = calculator.calculate_difference(1985, 2023)
    print(result3)