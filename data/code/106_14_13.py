from datetime import datetime

class YearDifferenceCalculator:
    @staticmethod
    def calculate_difference(year1: int, year2: int) -> int:
        return abs(year1 - year2)

if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    calculator = YearDifferenceCalculator()
    difference = calculator.calculate_difference(year1, year2)
    print(f"Year 1: {year1}")
    print(f"Year 2: {year2}")
    print(f"The absolute difference between the years is: {difference}")