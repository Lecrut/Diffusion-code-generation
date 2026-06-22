from typing import Tuple

def validate_input(numbers: Tuple) -> None:
    if not numbers:
        raise ValueError("Input tuple is empty")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Tuple contains non-numeric types")

def calculate_average(numbers: Tuple) -> float:
    return sum(numbers) / len(numbers)

def average(numbers: Tuple) -> float:
    validate_input(numbers)
    return calculate_average(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40)
    print(average(sample_values))