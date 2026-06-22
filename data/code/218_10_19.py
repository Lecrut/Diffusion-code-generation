from typing import List
MAX_SAMPLE_SIZE = 100

def find_min_value(numbers: List[int]) -> int:
    return min(numbers)
if __name__ == '__main__':
    sample_values = [34, 23, 56, 12, 78, -9]
    minimum_value = find_min_value(sample_values)
    print(minimum_value)