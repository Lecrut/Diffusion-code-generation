from typing import List, Tuple

def compute_weighted_avg(data: List[Tuple[float, float]]) -> float:
    if not data:
        return 0.0
    numerator = 0.0
    denominator = 0.0
    for value, weight in data:
        numerator += value * weight
        denominator += weight
    if denominator == 0:
        return 0.0
    return numerator / denominator

if __name__ == '__main__':
    readings = [
        (100.0, 1),
        (150.0, 2),
        (200.0, 3)
    ]
    avg = compute_weighted_avg(readings)
    print(avg)