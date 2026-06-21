from typing import List, Tuple

class MinMaxCalculator:
    MIN_INF = float('-inf')
    MAX_INF = float('inf')

    @staticmethod
    def min_max(values: List[float]) -> Tuple[float, float]:
        if not values:
            raise ValueError("Input collection cannot be empty")
        
        current_min = MinMaxCalculator.MIN_INF
        current_max = MinMaxCalculator.MAX_INF
        
        for value in values:
            if value < current_min:
                current_min = value
            if value > current_max:
                current_max = value
                
        return (current_min, current_max)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, 9.87]
    calculator = MinMaxCalculator()
    result = calculator.min_max(sample_values)
    print(result)