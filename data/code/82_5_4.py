class YearDifferenceCalculator:
    def __init__(self, year1, year2):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self):
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator(2023, 1990)
    print(calculator.calculate_difference())