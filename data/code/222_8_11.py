from typing import List

def find_min(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 10]
    print(find_min(sample_numbers))