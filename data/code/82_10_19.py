class YearDifferenceCalculator:
    START_YEAR = 1985
    END_YEAR = 2023

    @staticmethod
    def calculate_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.calculate_difference(YearDifferenceCalculator.START_YEAR, YearDifferenceCalculator.END_YEAR)
    print(result)