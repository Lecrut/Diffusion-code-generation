from typing import Sequence

class MeanCalculator:
    def __init__(self, values: Sequence[float]):
        if not values:
            raise ValueError("The sequence cannot be empty")
        self.values = values

    def calculate_mean(self) -> float:
        total = sum(self.values)
        count = len(self.values)
        return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = MeanCalculator(sample_values)
    mean_value = calculator.calculate_mean()
    print(f"The mean of the sequence is: {mean_value}")