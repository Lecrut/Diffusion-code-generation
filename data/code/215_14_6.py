from typing import List

def find_largest_value(numbers: List[int]) -> int:
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(find_largest_value(sample_numbers))