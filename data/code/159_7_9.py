from typing import List

def filter_odd_numbers(numbers: List[int]) -> List[int]:
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 10, 12]
    result = filter_odd_numbers(sample_values)
    print(result)