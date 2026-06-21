from typing import List

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers: List[float]) -> float:
        if not numbers:
            return 0.0
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average

if __name__ == '__main__':
    sample_data = [25, 35, 45, 55, 65]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_data)
    print(result)