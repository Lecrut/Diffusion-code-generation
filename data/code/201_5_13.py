from typing import List
import math

class AverageCalculator:
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def add_number(self, number: float) -> None:
        self.total += number
        self.count += 1

    def calculate_average(self) -> float:
        if self.count == 0:
            return 0.0
        return math.fsum([self.total]) / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    for number in sample_numbers:
        calculator.add_number(number)
    print("Average:", calculator.calculate_average())