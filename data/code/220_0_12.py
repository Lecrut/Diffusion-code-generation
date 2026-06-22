from typing import List
import statistics

def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    try:
        average = calculate_average(sample_numbers)
        print(average)
    except ValueError as e:
        print(e)