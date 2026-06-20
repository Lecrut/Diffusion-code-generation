class YearDifferenceCalculator:
    @staticmethod
    def absolute_difference(year1: int, year2: int) -> int:
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    print(calculator.absolute_difference(2060, 1980))
    print(calculator.absolute_difference(1970, 2030))