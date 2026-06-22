from typing import List

def find_minimum(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    print(find_minimum(sample_values))