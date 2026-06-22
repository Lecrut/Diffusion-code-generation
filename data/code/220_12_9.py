from typing import Tuple

def calculate_average(numbers: Tuple[float]) -> float:
    if not numbers:
        raise ValueError("The tuple cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = (10.5, 20.3, 30.7)
    average = calculate_average(sample_data)
    print(average)