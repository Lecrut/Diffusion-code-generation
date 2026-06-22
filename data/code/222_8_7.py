from typing import List

def find_min(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    current_min = numbers[0]
    for number in numbers[1:]:
        if number < current_min:
            current_min = number
    
    return current_min

if __name__ == '__main__':
    sample_numbers = [6, 7, 3, 5, 2, 9, 4, 8, 1]
    print(find_min(sample_numbers))