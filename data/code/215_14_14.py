from typing import List

def find_largest_value(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list cannot be empty")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest_value(sample_values))