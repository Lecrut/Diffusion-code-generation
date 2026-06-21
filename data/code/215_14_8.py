from typing import List

def find_largest_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest_value(sample_values))