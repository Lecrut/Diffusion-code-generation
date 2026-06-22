from typing import List

def validate_input(numbers: List[int]) -> None:
    if not numbers:
        raise ValueError("Input list cannot be empty")

def find_minimum(numbers: List[int]) -> int:
    validate_input(numbers)
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)