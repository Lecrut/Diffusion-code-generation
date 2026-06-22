from typing import List
import statistics

def calculate_mean(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list is empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    try:
        mean_value = calculate_mean(sample_numbers)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)