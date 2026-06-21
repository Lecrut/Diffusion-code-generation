from typing import Sequence

class MeanCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_value(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self.total += value
        self.count += 1

    def calculate_mean(self) -> float:
        if self.count == 0:
            raise ValueError("No values added")
        return self.total / self.count

if __name__ == '__main__':
    calculator = MeanCalculator()
    calculator.add_value(10)
    calculator.add_value(20)
    calculator.add_value(30)
    calculator.add_value(40)
    calculator.add_value(50)
    mean = calculator.calculate_mean()
    print(f"The mean of the sequence is: {mean}")