from datetime import datetime

class YearDifferenceCalculator:
    def __init__(self, year1: int, year2: int):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self) -> int:
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator(2023, 1998)
    difference = calculator.calculate_difference()
    print(f"Year 1: {calculator.year1}")
    print(f"Year 2: {calculator.year2}")
    print(f"The absolute difference between the years is: {difference}")