from typing import List

def validate_input(data: List[float]) -> None:
    if not data:
        raise ValueError("Input list cannot be empty")

def calculate_average(numbers: List[float]) -> float:
    validate_input(numbers)
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [25, 35, 45, 55, 65]
    result = calculate_average(sample_data)
    print(result)