class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        return abs(year1 - year2)
if __name__ == '__main__':
    calculator = YearCalculator()
    year_a = 2023
    year_b = 1998
    difference = calculator.find_absolute_difference(year_a, year_b)
    print(difference)