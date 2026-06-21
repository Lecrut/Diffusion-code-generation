from typing import List, Tuple

def min_max(values: List[float]) -> Tuple[float, float]:
    if not values:
        raise ValueError("Input list cannot be empty")
    
    min_val = max_val = float('inf')
    
    for value in values:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, float('inf'), -float('inf')]
    print(min_max(sample_values))