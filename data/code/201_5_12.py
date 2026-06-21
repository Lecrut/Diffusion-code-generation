from typing import List
import math

def calculate_average(numbers: List[float]) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 3.75, 4.0]
    print(calculate_average(sample_values))