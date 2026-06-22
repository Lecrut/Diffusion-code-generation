from typing import List

def compute_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 15.7, 25.1, 30.9]
    result = compute_mean(sample_values)
    print(result)