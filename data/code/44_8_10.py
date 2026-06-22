from typing import List
import statistics

def compute_mean(numbers: List[int]) -> float:
    if not numbers:
        raise ValueError("The list of numbers must not be empty.")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_mean(sample_values)
    print(result)