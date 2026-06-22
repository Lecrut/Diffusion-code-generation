from typing import Tuple

def calculate_average(numbers: Tuple[float]) -> float:
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    print(calculate_average(sample_numbers))