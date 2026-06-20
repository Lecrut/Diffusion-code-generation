class YearDifferenceCalculator:
    def calculate_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    year_a = 2023
    year_b = 1998
    difference = calculator.calculate_difference(year_a, year_b)
    print(difference)