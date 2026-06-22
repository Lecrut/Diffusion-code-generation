from typing import List
MAX_INT = int(1000000000.0)

def find_maximum(numbers: List[int]) -> int:
    if not numbers:
        return None
    current_max = MAX_INT
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max
if __name__ == '__main__':
    sample_numbers = [15, 7, 22, 3, 45, 10]
    maximum_value = find_maximum(sample_numbers)
    print(maximum_value)