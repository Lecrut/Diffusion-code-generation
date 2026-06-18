from typing import List
def filter_positive_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 0, 3, 7, -2, 8, 9]
    result: List[int] = filter_positive_numbers(sample_data)