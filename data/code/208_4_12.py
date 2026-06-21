from typing import Sequence

def compute_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(compute_mean(sample_values))