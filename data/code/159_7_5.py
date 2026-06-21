from typing import List

def extract_odd_numbers(sequence: List[int]) -> List[int]:
    odd_elements = [element for element in sequence if element % 2 != 0]
    return odd_elements

if __name__ == '__main__':
    test_sequence = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 19]
    result = extract_odd_numbers(test_sequence)
    print(result)