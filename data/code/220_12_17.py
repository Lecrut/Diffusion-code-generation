from typing import Tuple

def calculate_average(numbers: Tuple[float]) -> float:
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10.5, 20.3, 30.7)
    print(calculate_average(sample_values))