from typing import List

def calculate_range(values: List[float]) -> float:
    return max(values) - min(values)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 7.8, 4.6]
    print(calculate_range(sample_values))