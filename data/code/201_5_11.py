from typing import List
import math

def calculate_average(numbers: List[float]) -> float:
    total = math.fsum(numbers)
    count = len(numbers)
    if count > 0:
        average = total / count
        return average
    else:
        return 0.0

if __name__ == '__main__':
    sample_numbers = [12.345, 67.890, 123.456, 789.012]
    print(calculate_average(sample_numbers))