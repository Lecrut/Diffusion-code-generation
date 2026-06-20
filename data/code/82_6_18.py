class YearDifferenceCalculator:
    @staticmethod
    def calculate_difference(year1, year2):
        return year1 - year2

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    print(calculator.calculate_difference(2024, 2020))
    print(calculator.calculate_difference(1990, 2000))
    print(calculator.calculate_difference(2025, 2025))
    print(calculator.calculate_difference(1800, 1900))