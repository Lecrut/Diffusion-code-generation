from typing import List

class FloatSumCalculator:
    @staticmethod
    def sum_elements(numbers: List[float]) -> float:
        return sum(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7]
    result = FloatSumCalculator.sum_elements(sample_values)
    print(result)