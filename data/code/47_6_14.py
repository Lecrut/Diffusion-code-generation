from typing import List

def calculate_mean(values: List[float]) -> float:
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_data: List[float] = [10.5, 20.3, 30.7, 40.1]
    result: float = calculate_mean(sample_data)
    print(result)