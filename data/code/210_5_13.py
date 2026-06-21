from typing import List

class RangeCalculator:
    def __init__(self, data: List[int]):
        self.data = data

    def calculate_range(self) -> int:
        if not self.data:
            return 0
        min_val = min(self.data)
        max_val = max(self.data)
        return max_val - min_val

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    calculator = RangeCalculator(sample_data)
    range_value = calculator.calculate_range()
    print(f"Range of the data: {range_value}")