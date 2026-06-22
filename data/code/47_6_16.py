from typing import List

def compute_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    values: List[float] = [1.5, 2.5, 3.5, 4.5, 5.5]
    result: float = compute_mean(values)
    print(result)