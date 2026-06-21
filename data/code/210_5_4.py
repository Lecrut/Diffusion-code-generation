from typing import List

def calculate_range(values: List[float]) -> float:
    if not values:
        raise ValueError("The list cannot be empty")
    return max(values) - min(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.7, 40.1]
    print(calculate_range(sample_values))