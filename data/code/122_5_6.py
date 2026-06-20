from typing import Tuple

class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number: int) -> None:
        self.total += number
        self.count += 1

    def get_average(self) -> float:
        return self.total / self.count if self.count > 0 else 0

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = (10, 20, 30, 40, 50)
    for number in sample_numbers:
        calculator.add_number(number)
        print(f"Current average: {calculator.get_average()}")