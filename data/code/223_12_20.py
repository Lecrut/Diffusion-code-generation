from typing import List

MAX_VALUE = float('-inf')

def find_maximum(numbers: List[int]) -> int:
    if not numbers:
        return None
    current_max = MAX_VALUE
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max

if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    maximum_value = find_maximum(sample_numbers)
    print(maximum_value)