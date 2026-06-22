from typing import List
import math

def get_minimum(values: List[float]) -> float:
    if not values:
        raise ValueError("List must not be empty")
    
    min_val = math.inf
    
    for value in values:
        if value < min_val:
            min_val = value
            
    return min_val

if __name__ == '__main__':
    sample_values: List[float] = [5.5, 2.1, 8.9, 1.3, 9.2, 4.4]
    result: float = get_minimum(sample_values)
    print(result)