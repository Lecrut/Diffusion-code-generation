from typing import List

def find_min(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [34, 23, 56, 12, 78, -9]
    print(find_min(sample_values))