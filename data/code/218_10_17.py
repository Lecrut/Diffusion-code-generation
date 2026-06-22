from typing import List

def find_min(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [34, 23, 56, 12, 78, -9]
    minimum_value = find_min(sample_values)
    print(minimum_value)