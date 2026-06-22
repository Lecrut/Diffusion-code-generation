from typing import List

def find_max_value(numbers: List[int]) -> int:
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_max_value(sample_numbers))