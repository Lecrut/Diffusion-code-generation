from typing import Tuple

class NumericAverageCalculator:
    @staticmethod
    def calculate_average(numbers: Tuple[int, float]) -> float:
        if not numbers:
            raise ValueError("Input tuple is empty")
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Tuple contains non-numeric types")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = NumericAverageCalculator()
    sample_values = (10, 20, 30, 40)
    average = calculator.calculate_average(sample_values)
    print(average)