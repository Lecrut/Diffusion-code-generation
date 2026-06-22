from typing import List

def find_min(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 1, 5]
    print(find_min(sample_numbers))