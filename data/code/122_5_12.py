from typing import Tuple

AVERAGE_CALCULATION_CONSTANT = 1 / len((10, 20, 30, 40, 50))

def calculate_average(numbers: Tuple[int]) -> float:
    return sum(numbers) * AVERAGE_CALCULATION_CONSTANT

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    average = calculate_average(sample_numbers)
    print(f"The average is: {average}")