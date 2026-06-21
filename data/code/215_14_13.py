from typing import List

def find_largest_value(numbers: List[int]) -> int:
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [15, 8, 22, 3, 19]
    print(find_largest_value(sample_values))