from typing import List

def find_min(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min(sample_numbers))