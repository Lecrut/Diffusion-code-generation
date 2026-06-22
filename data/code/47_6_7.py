from typing import List

def calculate_mean(values: List[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: List[float] = [10.5, 20.75, 15.25, 30.0, 25.5]
    result: float = calculate_mean(sample_values)
    print(result)