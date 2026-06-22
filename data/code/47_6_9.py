from typing import List

def compute_mean(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    values = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = compute_mean(values)
    print(result)