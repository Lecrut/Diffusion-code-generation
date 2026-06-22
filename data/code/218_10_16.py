from typing import List

def find_min_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [10, 45, 23, -7, 0, 89]
    minimum_value = find_min_value(sample_values)
    print(minimum_value)