from typing import List
import math

def compute_average(values: List[float]) -> float:
    total = math.fsum(values)
    count = len(values)
    if count > 0:
        average = total / count
        return average
    else:
        return 0.0

if __name__ == '__main__':
    sample_values = [1.23, 4.56, 7.89]
    result = compute_average(sample_values)
    print(result)