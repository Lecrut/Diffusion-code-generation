from typing import List

def find_min(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("The list cannot be empty")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_numbers = [12, 4, 8, 5, 3, 17, 9]
    print(find_min(sample_numbers))