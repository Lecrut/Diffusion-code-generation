class YearDifferenceCalculator:
    def calculate_difference(self, year1, year2):
        if not (isinstance(year1, int) and isinstance(year2, int)):
            raise ValueError("Both inputs must be integers.")
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    difference = calculator.calculate_difference(2024, 1999)
    print(difference)