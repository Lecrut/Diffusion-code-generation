from typing import List

def find_largest_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest_value(sample_values))