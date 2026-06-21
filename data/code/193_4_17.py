from typing import List

class FloatSumCalculator:
    def __init__(self, numbers: List[float]):
        self._numbers = numbers
    
    def calculate_sum(self) -> float:
        return sum(self._numbers)

if __name__ == '__main__':
    sample_floats = [1.5, 2.3, 3.7]
    calculator = FloatSumCalculator(sample_floats)
    result = calculator.calculate_sum()
    print(result)