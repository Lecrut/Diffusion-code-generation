from typing import List
def filter_positive_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 0, 3, 7, 20, -99]
    result_set: List[int] = filter_positive_numbers(sample_data)