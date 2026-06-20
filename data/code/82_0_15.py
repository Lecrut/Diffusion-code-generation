class YearCalculator:
    MIN_YEAR = 1753

    @staticmethod
    def calculate_year_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    difference = calculator.calculate_year_difference(2023, 1998)
    print(difference)