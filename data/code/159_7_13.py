from typing import List

def extract_odd_integers(numbers: List[int]) -> List[int]:
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

if __name__ == '__main__':
    sample_sequence = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 19]
    output = extract_odd_integers(sample_sequence)
    print(output)