from typing import Sequence

def compute_mean(values: Sequence[float]) -> float:
    if len(values) == 0:
        return 0.0
    total: float = 0.0
    for val in values:
        total += val
    return total / len(values)

if __name__ == '__main__':
    data: list[float] = [2.5, 4.5, 6.5, 8.5, 10.5]
    average: float = compute_mean(data)
    print(average)