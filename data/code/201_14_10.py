from typing import List

def validate_data(data: List[float]) -> bool:
    return all(isinstance(x, (int, float)) for x in data) and len(data) > 0

def calculate_average(numbers: List[float]) -> float:
    if not validate_data(numbers):
        raise ValueError("Data must be a non-empty list of numbers")
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_average(sample_data))