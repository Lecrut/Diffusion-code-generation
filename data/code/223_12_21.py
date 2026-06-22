from typing import List

def find_max_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    current_max = numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
    return current_max

if __name__ == '__main__':
    sample_numbers = [25, 78, 34, 65, 90, 12]
    max_value = find_max_value(sample_numbers)
    print(max_value)