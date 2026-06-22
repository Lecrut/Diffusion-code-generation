from typing import List

def find_maximum_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list is empty")
    
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    
    return max_value

if __name__ == '__main__':
    sample_values = [23, 45, 67, 89, 34, 56]
    maximum_value = find_maximum_value(sample_values)
    print(maximum_value)