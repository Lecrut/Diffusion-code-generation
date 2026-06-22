from typing import List
import statistics

def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 4.2, 5.1, 6.7]
    try:
        average = calculate_average(sample_values)
        print(average)
    except ValueError as e:
        print(e)