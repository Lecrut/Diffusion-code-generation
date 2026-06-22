from typing import Tuple

class AverageCalculator:
    def calculate_average(self, numbers: Tuple[int, float]) -> float:
        if not numbers:
            raise ValueError("Input tuple is empty")
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Tuple contains non-numeric types")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = (10, 20, 30, 40)
    average_result = calculator.calculate_average(sample_values)
    print(average_result)