from typing import List, Tuple

def compute_min_max(values: List[float]) -> Tuple[float, float]:
    if not values:
        raise ValueError("Input list cannot be empty")
    
    min_val = math.inf
    max_val = -math.inf
    
    for value in values:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [4.56, 3.14, 2.71, -1.23, 0.57]
    result = compute_min_max(sample_values)
    print(result)