from typing import List

def collect_odd_numbers(numbers: List[int]) -> List[int]:
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = collect_odd_numbers(sample_list)
    print(result)