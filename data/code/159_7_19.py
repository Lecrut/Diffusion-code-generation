from typing import List

def is_odd(number: int) -> bool:
    return number % 2 != 0

def collect_odd_numbers(numbers: List[int]) -> List[int]:
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list of integers.')
    if not all((isinstance(num, int) for num in numbers)):
        raise ValueError('All elements in the list must be integers.')
    return [num for num in numbers if is_odd(num)]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = collect_odd_numbers(sample_list)
    print(result)