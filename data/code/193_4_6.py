from typing import List

class FloatSummator:
    def __init__(self, data: List[float]):
        self.data = data
    
    def calculate_sum(self) -> float:
        return sum(self.data)

if __name__ == '__main__':
    sample_floats = [1.5, 2.3, 3.7]
    summator = FloatSummator(sample_floats)
    total = summator.calculate_sum()
    print(total)