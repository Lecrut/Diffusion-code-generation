from typing import Tuple

def validate_numbers(numbers: Tuple[int]) -> None:
    if not numbers:
        raise ValueError("The tuple is empty")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the tuple must be integers")

def calculate_average(numbers: Tuple[int]) -> float:
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    average = calculate_average(sample_numbers)
    print(f"The average is: {average}")