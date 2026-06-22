from typing import Tuple

def average(numbers: Tuple[float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Tuple contains non-numeric types")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10.5, 20.3, 30.7)
    print(average(sample_values))