from typing import Tuple

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers: Tuple[int]) -> float:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    calculator = AverageCalculator()
    average = calculator.calculate_average(sample_numbers)
    print(f"The average is: {average}")