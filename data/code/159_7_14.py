from typing import List

def filter_odd_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(sample_values)
    print(result)