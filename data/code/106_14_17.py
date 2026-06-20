from datetime import datetime

class YearDifference:
    def __init__(self, year1: int, year2: int):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self) -> int:
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    difference_instance = YearDifference(year1, year2)
    print(f"Year 1: {year1}")
    print(f"Year 2: {year2}")
    print(f"The absolute difference between the years is: {difference_instance.calculate_difference()}")