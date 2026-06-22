from typing import List

def compute_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: List[float] = [3.5, 7.2, 4.8, 9.1, 2.4]
    result: float = compute_mean(sample_values)
    print(result)