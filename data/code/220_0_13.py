from typing import List
import statistics

def calculate_mean(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    try:
        result = calculate_mean(sample_values)
        print(result)
    except ValueError as e:
        print(e)