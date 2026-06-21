from typing import List, Tuple

def min_max(collection: List[float]) -> Tuple[float, float]:
    if not collection:
        raise ValueError("Input collection cannot be empty")
    
    min_val = max_val = float('inf')
    
    for num in collection:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, -1.414]
    print(min_max(sample_values))