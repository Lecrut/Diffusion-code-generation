from typing import List

def find_largest_value(numbers: List[int]) -> int:
    return max(numbers)

if __name__ == '__main__':
    sample_values = [7, 3, 9, 12, 5]
    largest_value = find_largest_value(sample_values)
    print(largest_value)