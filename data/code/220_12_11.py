from typing import Tuple

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers: Tuple[int]) -> float:
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = (1, 2, 3)
    average = calculator.calculate_average(sample_data)
    print(average)