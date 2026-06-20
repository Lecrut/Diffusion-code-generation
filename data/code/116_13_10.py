from typing import Tuple

def validate_input(numbers: Tuple[int, int, int]) -> None:
    if not isinstance(numbers, tuple):
        raise ValueError("Input must be a tuple.")
    if len(numbers) != 3:
        raise ValueError("Tuple must contain exactly three elements.")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements of the tuple must be integers.")

def sum_three_integers(numbers: Tuple[int, int, int]) -> int:
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30)
    result = sum_three_integers(sample_values)
    print(result)