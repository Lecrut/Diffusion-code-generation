from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = (10, 20, 30)
    average = calculate_average(sample_data)
    print(average)