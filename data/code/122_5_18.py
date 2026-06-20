from typing import Tuple

class AverageCalculator:
    def __init__(self, numbers: Tuple[int]):
        self.numbers = numbers

    def calculate_average(self) -> float:
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    calculator = AverageCalculator(sample_numbers)
    average = calculator.calculate_average()
    print(f"The average is: {average}")