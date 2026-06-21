from typing import List

def is_valid_input(data: List[int]) -> bool:
    return all(isinstance(item, int) for item in data)

def collect_odd_numbers(numbers: List[int]) -> List[int]:
    if not is_valid_input(numbers):
        raise ValueError("Input must be a list of integers")
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = collect_odd_numbers(sample_list)
    print(result)