from typing import Tuple
import math

def min_max(collection: list) -> Tuple[float, float]:
    if not collection:
        raise ValueError("Input collection cannot be empty")
    
    min_val = math.inf
    max_val = -math.inf
    
    for num in collection:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.41, 1.618]
    print(min_max(sample_values))