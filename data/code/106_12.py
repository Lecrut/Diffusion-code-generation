class DateCalculator:
    def get_difference(self, year1, year2):
        return abs(year1 - year2)
if __name__ == '__main__':
    calculator = DateCalculator()
    year_a = 2020
    year_b = 1995
    difference = calculator.get_difference(year_a, year_b)
    print(difference)