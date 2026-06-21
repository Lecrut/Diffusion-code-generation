from typing import List

def calculate_range(values: List[float]) -> float:
    if not values or len(values) < 2:
        raise ValueError("List must contain at least two numeric values")
    return max(values) - min(values)

if __name__ == '__main__':
    sample_values = [10.5, 3.2, 7.8, 15.4, 2.1]
    print(calculate_range(sample_values))