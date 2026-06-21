from typing import List

def extract_odd_numbers(sequence: List[int]) -> List[int]:
    return [number for number in sequence if number % 2 != 0]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = extract_odd_numbers(sample_sequence)
    print(result)