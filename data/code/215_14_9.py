from typing import List

def find_largest_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list is empty")
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_values = [7, 2, 9, 3, 5]
    print(find_largest_value(sample_values))