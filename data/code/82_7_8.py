class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    result = calculator.find_absolute_difference(2023, 1987)
    print(result)