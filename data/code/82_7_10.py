class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        if not isinstance(year1, int) or not isinstance(year2, int):
            raise ValueError("Both inputs must be integers")
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    result = calculator.find_absolute_difference(2023, 2025)
    print(result)