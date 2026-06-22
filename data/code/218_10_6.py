from typing import List

def find_min_value(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5]
    print(find_min_value(sample_values))