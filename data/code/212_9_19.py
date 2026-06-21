from typing import List, Tuple

class MinMaxCalculator:
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    @staticmethod
    def min_max(values: List[float]) -> Tuple[float, float]:
        if not values:
            raise ValueError("Input list cannot be empty")
        
        min_val = MinMaxCalculator.MIN_VALUE
        max_val = MinMaxCalculator.MAX_VALUE
        
        for value in values:
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value
                
        return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, 9.87]
    calculator = MinMaxCalculator()
    result = calculator.min_max(sample_values)
    print(result)