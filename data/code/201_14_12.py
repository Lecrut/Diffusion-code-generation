from typing import List

def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("The input list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    try:
        print(calculate_average(sample_data))
    except ValueError as e:
        print(e)