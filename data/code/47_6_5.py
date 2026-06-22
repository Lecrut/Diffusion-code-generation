from typing import List

def compute_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 4.7, 5.1, 3.9]
    result = compute_mean(sample_values)
    print(result)