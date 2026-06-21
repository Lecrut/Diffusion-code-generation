from typing import List
import math

def validate_numbers(numbers: List[float]) -> bool:
    if not numbers:
        return False
    for num in numbers:
        if not isinstance(num, float):
            return False
    return True

def calculate_average(numbers: List[float]) -> float:
    if not validate_numbers(numbers):
        raise ValueError("Input must be a non-empty list of floats")
    total = math.fsum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(calculate_average(sample_numbers))