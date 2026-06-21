from typing import List, Tuple

def min_max(collection: List[float]) -> Tuple[float, float]:
    if not collection:
        raise ValueError("Input collection cannot be empty")
    min_val = max_val = float('inf')
    for value in collection:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.57, -1.23, 9.87]
    print(min_max(sample_values))