from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = (15, 25, 35, 45)
    result = calculate_average(sample_data)
    print(result)