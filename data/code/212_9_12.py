from typing import Tuple, List

class MinMaxCalculator:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = -float('inf')

    def add_value(self, value: float) -> None:
        if value < self.min_val:
            self.min_val = value
        if value > self.max_val:
            self.max_val = value

    def get_min_max(self) -> Tuple[float, float]:
        return (self.min_val, self.max_val)

if __name__ == '__main__':
    calculator = MinMaxCalculator()
    sample_values = [3.14, 2.71, 0.577, 1.618]
    for value in sample_values:
        calculator.add_value(value)
    result = calculator.get_min_max()
    print(result)