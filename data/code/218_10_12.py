from typing import List

def find_minimum(numbers: List[int]) -> int:
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)