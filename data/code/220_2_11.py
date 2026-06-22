from typing import Tuple

def average(numbers: Tuple[int, float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    print(average(sample_values))