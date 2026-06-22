from typing import List

def compute_mean(values: List[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: List[float] = [1.5, 2.5, 3.5, 4.5, 5.5]
    result: float = compute_mean(sample_values)
    print(result)