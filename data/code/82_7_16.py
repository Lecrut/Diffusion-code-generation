class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    print(calculator.find_absolute_difference(10, 5))
    print(calculator.find_absolute_difference(2023, 2025))
    print(calculator.find_absolute_difference(1998, 2000))