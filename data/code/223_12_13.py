from typing import List

def find_maximum(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    current_max = numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
    
    return current_max

if __name__ == '__main__':
    sample_numbers = [15, 7, 22, 3, 45, 10]
    try:
        maximum_value = find_maximum(sample_numbers)
        print(maximum_value)
    except ValueError as e:
        print(e)