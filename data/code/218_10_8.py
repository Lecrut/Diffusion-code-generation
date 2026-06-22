from typing import List

def find_min_value(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_value(sample_values))