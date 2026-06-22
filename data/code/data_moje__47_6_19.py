from typing import List

def compute_mean(values: List[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: List[float] = [10.0, 20.5, 30.0, 40.25, 50.0]
    result: float = compute_mean(sample_values)
    print(result)