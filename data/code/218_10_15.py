from typing import List

def find_min(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_min(sample_numbers))