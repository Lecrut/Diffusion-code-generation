from typing import List, Tuple
import math

def min_max(collection: List[float]) -> Tuple[float, float]:
    if not collection:
        raise ValueError("Input collection is empty")
    
    minimum = math.inf
    maximum = -math.inf
    
    for value in collection:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.577, 1.618, -1.414]
    print(min_max(sample_values))