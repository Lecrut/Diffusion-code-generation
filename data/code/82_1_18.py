class YearDifferenceCalculator:
    def calculate_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.calculate_difference(2024, 1999)
    print(result)