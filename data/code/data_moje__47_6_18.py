from typing import List

def compute_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_data = [10.5, 20.25, 30.75, 40.0, 50.5]
    result = compute_mean(sample_data)
    print(result)