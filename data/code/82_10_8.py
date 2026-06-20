class YearDifferenceCalculator:
    def calculate_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    start_year = 1985
    end_year = 2023
    result = calculator.calculate_difference(start_year, end_year)
    print(result)