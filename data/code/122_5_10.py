from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0.0

if __name__ == '__main__':
    sample_numbers = (5, 10, 15, 20, 25)
    average = calculate_average(sample_numbers)
    print(f"The average is: {average}")