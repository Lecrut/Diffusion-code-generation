from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    try:
        average = calculate_average(sample_numbers)
        print(f"The average is: {average}")
    except ValueError as e:
        print(e)