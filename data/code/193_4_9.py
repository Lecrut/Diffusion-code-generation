from typing import List

class FloatSummator:
    def __init__(self, numbers: List[float]):
        self._numbers = numbers
    
    def calculate_sum(self) -> float:
        return sum(self._numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7]
    summator = FloatSummator(sample_values)
    result = summator.calculate_sum()
    print(result)